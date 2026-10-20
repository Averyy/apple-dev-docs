# options

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The options dictionary that was used to create the shape.

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
var options: [SCNPhysicsShape.Option : Any]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,id> * options;
```

#### Discussion

You provide this dictionary in the [`init(geometry:options:)`](./init%28geometry,options%29.md) or [`init(node:options:)`](./init%28node,options%29.md) method. Use this dictionary along with the [`sourceObject`](./sourceobject.md) property to recover the information that was used to create the shape.

If the shape was created with the [`init(shapes:transforms:)`](./init%28shapes,transforms%29.md) method, this property’s value is `nil`.

## See Also

### Getting Information About a Shape
- [var sourceObject: Any](./sourceobject.md)
  The object that was used to create the shape.
- [var transforms: [NSValue]?](./transforms.md)
  The array of transforms that was used to create a compound shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsshape/options)*