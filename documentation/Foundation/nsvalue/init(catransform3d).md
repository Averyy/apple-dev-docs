# init(CATransform3D:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified CoreAnimation transform structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(CATransform3D t: CATransform3D)
```

```swift
init(caTransform3D t: CATransform3D)
```

```objc
+ (NSValue *) valueWithCATransform3D:(CATransform3D) t;
```

## Return Value

A new value object that contains the transform information.

## Parameters

- `t`: The value for the new object.

## See Also

### Related Documentation
- [struct CATransform3D](../../QuartzCore/catransform3d.md)
  The standard transform matrix used throughout Core Animation.
### Working with CoreAnimation Transform Values
- [var caTransform3DValue: CATransform3D](./catransform3dvalue.md)
  The CoreAnimation transform structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(catransform3d:))*