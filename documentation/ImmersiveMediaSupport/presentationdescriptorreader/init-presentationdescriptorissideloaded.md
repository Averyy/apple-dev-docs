# init(presentationDescriptor:isSideloaded:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an instance containing the specified presentation descriptor.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(presentationDescriptor: PresentationDescriptor, isSideloaded: Bool = false)
```

## Parameters

- `presentationDescriptor`: Current presentation commands to be used/parsed.
- `isSideloaded`: Signals the player this is a sideloaded dynamic metadata and not real-time - in that case   the player will not delete old commands as playback continues (to support seek)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/init(presentationdescriptor:issideloaded:))*