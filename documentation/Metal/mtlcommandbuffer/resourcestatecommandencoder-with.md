# resourceStateCommandEncoder(with:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a resource state command encoder from a descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func resourceStateCommandEncoder(with resourceStatePassDescriptor: MTLResourceStatePassDescriptor) -> (any MTLResourceStateCommandEncoder)?
```

#### Discussion

Use an [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) instance’s methods to create a pass that updates the state of one or more sparse textures.

## Parameters

- `resourceStatePassDescriptor`: An   instance that configures the   the method returns.

## See Also

- [func makeResourceStateCommandEncoder() -> (any MTLResourceStateCommandEncoder)?](mtlcommandbuffer/makeresourcestatecommandencoder.md)
  Creates a resource state command encoder that uses default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/resourcestatecommandencoder(with:))*