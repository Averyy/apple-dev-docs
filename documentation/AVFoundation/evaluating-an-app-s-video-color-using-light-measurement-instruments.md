# Evaluating an app’s video color using light-measurement Instruments

**Framework**: AVFoundation

Measure front-of-screen luminance by using test pattern files with a spectroradiometer or colorimeter.

#### Overview

Evaluate the color characteristics of your AVFoundation-based app or workflow using test pattern files. Output these files to a spectroradiometer or colorimeter to measure the front-of-screen (FoS) luminance, and compare your measurements against the expected values.

##### Measure Fos Luminance

Use the test files from the `SDR_BT709_HDTV` folder (see “Color Test Patterns” on the [`AVFoundation Developer Page`](https://developer.apple.comhttps://developer.apple.com/av-foundation/)) with a measuring instrument such as a spectroradiometer or colorimeter to measure the FoS luminance. Take your measurements after aligning the instrument to the center of the display in a dark room to prevent stray light or glare from influencing the measurements. You may see some variation in the readings depending on your instrument’s tolerances and its calibration.

Use the luminance ramp test pattern files in the folder `SDR_BT709_HDTV` to measure the FoS luminance. Open the test pattern movie files in your app or the QuickTime Player app, then measure and compare the results against those shown below. If you encounter conflicting results, see [`Ensure accurate color application of your app’s video`](evaluating-an-app-s-video-color#Ensure-accurate-color-application-of-your-apps-video.md) to make certain your app takes advantage of the color-management capabilities of macOS.

The following list summarizes the FoS luminance expectations (output in nits) on macOS platforms for video files tagged as BT.709 (NCLC = 1-1-1).

The system uses a 1.961 gamma based on the assumption of a bright surround environment. The linear brightness attenuation varies between 0 and 1 and is dependent on the position of the display’s brightness slider. Reference white nits is the peak luminance capability of the Mac display.

Reference white nits is the peak luminance capability of the external TV or monitor. The display’s EOTF (electro-optical transfer function) gamma is the gamma used by the TV or monitor to decode the input signal to linear light.

The system uses a 1.961 gamma based on the assumption of a bright surround environment, the same as the macOS internal displays. The linear brightness attenuation varies between 0 and 1 and is dependent on the position of the display’s brightness slider. Reference white nits is the peak SDR (standard dynamic range) luminance capability of the mode in the Pro Display XDR display, which is set to 500 nits for both of the Apple reference modes.

Reference white nits is the peak SDR luminance capability of HDR Video (P3 - ST 2084) mode, which is set to 100 nits.

(where a and b are derived as per [`Recommendation ITU-R BT.1886`](https://developer.apple.comhttps://www.itu.int/dms_pubrec/itu-r/rec/bt/R-REC-BT.1886-0-201103-I!!PDF-E.pdf))

a = (Lw ^ (1/gamma) - Lb ^ (1/gamma))^(gamma)

b = Lb ^ (1/gamma) / ((Lw ^ (1/gamma) - Lb ^ (1/gamma))

Lw = 100.0 nits

Lb = 0.0005 nits

gamma = 2.4

Reference white nits (SDR maximum luminance) and system gamma boost (≥ 1.0) are set while creating a custom reference mode.

## See Also

- [Evaluating video using QuickTime test pattern files](evaluating-video-using-quicktime-test-pattern-files.md)
  Check color reproduction of your app or workflow by using test pattern files.
- [Evaluating an app’s video color using video test equipment](evaluating-an-app-s-video-color-using-video-test-equipment.md)
  Output test pattern files to a vectorscope or waveform analyzer to review the video signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/evaluating-an-app-s-video-color-using-light-measurement-instruments)*