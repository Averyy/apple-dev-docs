# transforms

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The array of transforms that was used to create a compound shape.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var transforms: [NSValue]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSArray<NSValue *> * transforms;
```

## Discussion

You provide this array of [`NSValue`](../../Foundation/nsvalue.md) objects, each containing an [`SCNMatrix4`](../scnmatrix4-swift.struct.md) value, in the [`init(shapes:transforms:)`](./init%28shapes,transforms%29.md) method to create a compound shape. Use this array along with the [`sourceObject`](./sourceobject.md) property to recover the information that was used to create the shape.

If the shape was created with the [`init(geometry:options:)`](./init%28geometry,options%29.md) or [`init(node:options:)`](./init%28node,options%29.md) method, this property’s value is `nil`.

## See Also

### Getting Information About a Shape
- [var sourceObject: Any](./sourceobject.md)
  The object that was used to create the shape.
- [var options: [SCNPhysicsShape.Option : Any]?](./options.md)
  The options dictionary that was used to create the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/transforms)*