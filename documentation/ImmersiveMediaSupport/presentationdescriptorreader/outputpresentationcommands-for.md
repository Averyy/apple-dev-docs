# outputPresentationCommands(for:)

**Framework**: Immersive Media Support  
**Kind**: method

This function returns all presentation commands to be muxed into an MOV during an `AVAssetWriter` session. Don’t use this function for playback rendering.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func outputPresentationCommands(for time: CMTime) -> [PresentationCommand]?
```

#### Return Value

An array of PresentationCommand instances representing the commands that need to be included in the output file for that PTS.

## Parameters

- `time`: PTS time to query for commands


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/outputpresentationcommands(for:))*