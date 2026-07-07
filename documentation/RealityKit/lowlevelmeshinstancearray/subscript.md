# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Returns the mesh instance at the given index, or `nil` if the slot is unoccupied.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final subscript(position: Int) -> LowLevelMeshInstance? { get }
```

#### Return Value

The [`LowLevelMeshInstance`](lowlevelmeshinstance.md) at `position`, or `nil` if the slot is empty.

## Parameters

- `position`: The slot index to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshinstancearray/subscript(_:))*