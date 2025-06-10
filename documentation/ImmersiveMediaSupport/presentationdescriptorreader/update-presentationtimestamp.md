# update(presentationTimeStamp:)

**Framework**: Immersive Media Support  
**Kind**: method

Update is called by the application (e.g. render/playback loop) to update the publishers exported by PresentationDescriptorReader

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func update(presentationTimeStamp: CMTime)
```

## Parameters

- `presentationTimeStamp`: The current presentation time to query metadata.

## See Also

- [func outputPresentationCommands(for: CMTime, including: [PresentationCommandType]) -> [any PresentationCommand]?](presentationdescriptorreader/outputpresentationcommands(for:including:).md)
  This function returns all presentation commands to be muxed into an MOV during an AVAssetWriter session. It’s not supposed to be used for playback rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/update(presentationtimestamp:))*