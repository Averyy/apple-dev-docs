# Adjusting anchor loudness

**Framework**: HTTP Live Streaming

Adjust anchor loudness when measurements of speech-gated loudness for a full mix may be inaccurate, such as when speech activity is low.

#### Overview

Apply the adjustment method below to improve the consistency of your anchor loudness, or standard, value for low speech activity. The method’s basis is a statistical model of anchor loudness for a large variety of long-form content that takes advantage of the correlation with other loudness-based measurements. The method uses the following measurements:

- Speech-gated loudness
- Speech activity that derives from a speech detector
- Program loudness (ITU-R BS.1770-4)
- Top value of LRA (loudness range) (EBU Tech 3342)

For low speech activity, the model ignores the speech-gated loudness value and computes anchor loudness from the other three measurements. A gradual transition from the model to the measured, speech-gated loudness occurs as the speech activity increases.

The following examples and source code show how to calculate anchor loudness using program loudness and speech-gated loudness.

##### Determine Anchor Loudness Using Different Program Loudness Values

The following figure shows a visual representation of anchor loudness for an example with a speech-gated loudness of -27 LKFS (loudness, K-weighted, relative to full scale) and different program loudness values.

![Graph depicting calculated anchor loudness values for an example with a speech-gated loudness of -27 LKFS and various program loudness values. The y axis represents anchor loudness in LKFS, from -30 at the bottom to -20 at the top. The x axis represents the speech activity level, from 0 on the left to 1 on the right. Five lines correspond to various program loudness values in LKFS. The top value of LRA is 3 loudness units higher than the program loudness value.](https://docs-assets.developer.apple.com/published/cb2233e5249afbd0c413ca2f2f807f99/adjusting-anchor-loudness-1%402x.png)

The lines on the left correspond to the calculated anchor loudness as a result of the adjustment method. The labels for each line indicate the program loudness values. For low speech activity, anchor loudness increases with program loudness. For increasing speech activity, there’s a transition to the speech-gated loudness measurement.

The next figure displays anchor loudness for an example with speech-gated loudness of -27 LKFS and program loudness of -24 LKFS. The difference between top value of LRA and program loudness characterizes how dynamic the content is. The lines on the left correspond to the calculated anchor loudness as a result of the adjustment method. The labels for each line indicate the value of the loudness difference in loudness units (LU). The loudness difference correlates with anchor loudness, and the modeling results in lower anchor loudness for more dynamic content at low speech activity. As the speech activity increases, anchor loudness transitions to the measured speech-gated loudness.

![Graph depicting calculated anchor loudness values for an example with a speech-gated loudness of -27 LKFS and a program loudness of -24 LKFS. The y axis represents anchor loudness in LKFS, from -30 at the bottom to -20 at the top. The x axis represents the speech activity level, from 0 on the left to 1 on the right. Five lines correspond to various values between top value of LRA and program loudness.](https://docs-assets.developer.apple.com/published/daaae13428d19cc598f5e41dcc2d26f2/adjusting-anchor-loudness-2%402x.png)

The following source code includes a function to compute the adjusted anchor loudness value from the parameters in the preceding examples, which is applicable to long-form content.

```swift
enum AnchorLoudnessAdjustmentError: Error {
    case speechActivityOutOfBounds
}

/// Computes adjusted anchor loudness
/// - Parameters:
///   - programLoudness: The loudness (LKFS) produced by ITU-R BS.1770-4.
///   - speechLoudness: The loudness (LKFS) produced by ITU-R BS.1770-4 applied to the speech-gated content.
///   - activity: The ratio of speech-gated content duration and content duration.
///   - isLraTopPresent: If `true`, the top value of LRA measurement is available.
///   - lraTop: The loudness (LKFS) produced by taking the top value of loudness range according to EBU Tech 3342.
/// - Returns: Adjusted anchor loudness (LKFS)
func adjustedAnchorLoudnessFor(programLoudness: Double,
                               speechLoudness: Double,
                               activity: Double,
                               isLraTopPresent: Bool,
                               lraTop: Double) throws -> Double {
    guard (0...1).contains(activity) else {
        throw AnchorLoudnessAdjustmentError.speechActivityOutOfBounds
    }

    // Constants
    /// Ignore `speechLoudness` below this speech activity ratio.
    let activityLow = 0.17
    /// Keep `speechloudness` above this speech activity ratio.
    let activityHigh = 0.25
    /// The boundary for the difference of `anchorLoudness` and `programLoudness`.`
    let loudnessOffsetDefault = 3.0
    /// The upper limit for the difference of `programLoudness` and `anchorLoudness`.
    let loudnessOffsetMax = 8.0
    /// The lower limit for the difference of `programLoudness` and `anchorLoudness`.
    let loudnessOffsetMin = 0.0
    /// The upper limit for the difference of `programLoudness` and `speechLoudness`.
    let loudnessDiffMax = 8.0

    // Parameters for linear regression models.
    let model1ParamA = 6.452208
    let model1ParamB1 = 0.301736
    let model1ParamB2 = 0.881433
    let model2ParamA = 11.549024
    let model2ParamB = 0.362253

    var loudnessOffset = loudnessOffsetDefault
    var speechLoudnessBounded = speechLoudness
    var anchorLoudness = speechLoudness

    // Limit speech loudness to a reasonable range below program loudness.
    let diffLoudness = programLoudness - speechLoudnessBounded
    if diffLoudness > loudnessDiffMax {
        speechLoudnessBounded = programLoudness - loudnessDiffMax
    }
    if speechLoudnessBounded > programLoudness {
        speechLoudnessBounded = programLoudness
    }

    // Compute loudness offset from linear regression model.
    if isLraTopPresent {
        let plLraTop = max(0, lraTop - programLoudness)
        loudnessOffset = model1ParamA +
            model1ParamB1 * programLoudness +
            model1ParamB2 * plLraTop
    } else {
        loudnessOffset = model2ParamA + model2ParamB * programLoudness
    }

    // Clamp `loudnessOffset`.
    loudnessOffset = max(loudnessOffsetMin, min(loudnessOffset, loudnessOffsetMax))

    // Update anchor loudness according to activity level.
    if activity > activityHigh {
        anchorLoudness = speechLoudnessBounded
    } else {
        if activity > activityLow {
            let weight = (activity - activityLow) / (activityHigh - activityLow)
            anchorLoudness = weight * speechLoudnessBounded +
                (1 - weight) * (programLoudness - loudnessOffset)
        } else {
            anchorLoudness = programLoudness - loudnessOffset
        }
    }

    return anchorLoudness
}
```

## See Also

- [HTTP Live Streaming (HLS) authoring specification for Apple devices](hls-authoring-specification-for-apple-devices.md)
  Learn the requirements for live and on-demand audio and video content delivery using HLS.
- [Using content protection systems with HLS](using-content-protection-systems-with-hls.md)
  Adding encryption keys to media playlists
- [About the Common Media Application Format with HTTP Live Streaming (HLS)](about-the-common-media-application-format-with-http-live-streaming-hls.md)
  Learn the Common Media Application Format as it applies to HLS.
- [Enabling Low-Latency HTTP Live Streaming (HLS)](enabling-low-latency-http-live-streaming-hls.md)
  Add Low-Latency HLS to your content streams to maintain scalability.
- [Links to additional specifications and videos](links-to-additional-specifications-and-videos.md)
  Review additional specifications and documents.
- [Videos about HLS](videos-about-hls.md)
  Review informational videos about HTTP Live Streaming.
- [Providing metadata for xHE-AAC video soundtracks](providing-metadata-for-xhe-aac-video-soundtracks.md)
  Ensure volume normalization by including metadata for loudness and dynamic range control.
- [Providing JavaScript Object Notation (JSON) chapters](providing-javascript-object-notation-json-chapters.md)
  Prepare JSON chapters for HTTP Live Streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/http-live-streaming/adjusting-anchor-loudness)*