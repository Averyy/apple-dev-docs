# accessoryWithShape:position:

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a pointer accessory with the specified shape and position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) accessoryWithShape:(UIPointerShape *) shape position:(UIPointerAccessoryPosition) position;
```

## Parameters

- `shape`: One of the available [`UIPointerShape`](../uipointershape-swift.enum.md) shapes.
- `position`: One of the available [`UIPointerAccessory.Position`](./position-swift.struct.md) positions.

## See Also

### Creating a pointer accessory
- [+ arrowAccessoryWithPosition:](./arrowaccessorywithposition_.md)
  Creates a pointer accessory at the specified position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointeraccessory/accessorywithshape:position:)*