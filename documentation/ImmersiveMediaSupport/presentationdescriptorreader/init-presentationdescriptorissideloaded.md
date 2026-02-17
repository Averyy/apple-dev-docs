# init(presentationDescriptor:isSideloaded:)

**Framework**: Immersive Media Support  
**Kind**: init

Initializes an instance that contains the specified presentation descriptor.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(presentationDescriptor: PresentationDescriptor, isSideloaded: Bool = false)
```

## Parameters

- `presentationDescriptor`: The current presentation commands to use or parse.
- `isSideloaded`: Signals the player this is a sideloaded dynamic metadata and not real-time - in that case   the player will not delete old commands as playback continues (to support seek)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader/init(presentationdescriptor:issideloaded:))*