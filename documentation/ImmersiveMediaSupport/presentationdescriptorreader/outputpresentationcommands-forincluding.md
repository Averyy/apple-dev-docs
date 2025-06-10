# outputPresentationCommands(for:including:)

**Framework**: Immersive Media Support  
**Kind**: method

This function returns all presentation commands to be muxed into an MOV during an AVAssetWriter session. It’s not supposed to be used for playback rendering.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func outputPresentationCommands(for time: CMTime, including: [PresentationCommandType] = PresentationCommandType.allCases) -> [any PresentationCommand]?
```

#### Return Value

An array of PresentationCommand instances representing the commands that need to be included in the output file for that PTS.

## Parameters

- `time`: PTS time to query for commands
- `including`: Array of command types to include, defaults to all commands

## See Also

- [func update(presentationTimeStamp: CMTime)](presentationdescriptorreader/update(presentationtimestamp:).md)
  Update is called by the application (e.g. render/playback loop) to update the publishers exported by PresentationDescriptorReader


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/outputpresentationcommands(for:including:))*