# makeResourceStateCommandEncoder()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a resource state command encoder that uses default settings.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeResourceStateCommandEncoder() -> (any MTLResourceStateCommandEncoder)?
```

#### Discussion

Use an [`MTLResourceStateCommandEncoder`](mtlresourcestatecommandencoder.md) instance’s methods to create a pass that updates the state of one or more sparse textures.

## See Also

- [func resourceStateCommandEncoder(with: MTLResourceStatePassDescriptor) -> (any MTLResourceStateCommandEncoder)?](mtlcommandbuffer/resourcestatecommandencoder(with:).md)
  Creates a resource state command encoder from a descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/makeresourcestatecommandencoder())*