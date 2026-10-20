# init(_:position:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a pointer accessory with the specified shape and position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency convenience init(_ shape: UIPointerShape, position: UIPointerAccessory.Position)
```

## Parameters

- `shape`: One of the available [`UIPointerShape`](../uipointershape-swift.enum.md) shapes.
- `position`: One of the available [`UIPointerAccessory.Position`](./position-swift.struct.md) positions.

## See Also

### Creating a pointer accessory
- [class func arrow(UIPointerAccessory.Position) -> Self](./arrow%28_%29.md)
  Creates a pointer accessory with an arrow shape at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory/init(_:position:))*