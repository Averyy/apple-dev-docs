# makeBufferResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method

Creates a GPU-managed buffer resource from the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource
```

#### Return Value

A newly created [`LowLevelBufferResource`](lowlevelbufferresource.md).

#### Discussion

> **Note**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The capacity and alignment requirements for the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makebufferresource(descriptor:))*