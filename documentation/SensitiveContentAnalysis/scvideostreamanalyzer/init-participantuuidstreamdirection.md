# init(participantUUID:streamDirection:)

**Framework**: SensitiveContentAnalysis  
**Kind**: init

Creates a video stream analyzer for the given call participant and stream option.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
init(participantUUID: String, streamDirection: SCVideoStreamAnalyzer.StreamDirection) throws
```

#### Discussion

> ❗ **Important**:  This class works only when the Communication Safety parental control in Screen Time is enabled, or when the Sensitive Content Warnings setting is on. This method throws an error if both settings are off, or if the device doesn’t support analysis for the specified stream direction.

## Parameters

- `participantUUID`: A unique identifier that you provide to distinguish among multiple individuals on a conference call. Set this argument to the same value per person on the call, if your app supports multiple streams per person.
- `streamDirection`: An option that indicates whether the stream comes from the device’s camera or from a remote individual signed in to the call.

## See Also

- [SCVideoStreamAnalyzer.StreamDirection](scvideostreamanalyzer/streamdirection.md)
  Options for the different types of analyzed video streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensitivecontentanalysis/scvideostreamanalyzer/init(participantuuid:streamdirection:))*