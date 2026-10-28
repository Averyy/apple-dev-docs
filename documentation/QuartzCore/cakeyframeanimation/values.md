# values

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

An array of objects that specify the keyframe values to use for the animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var values: [Any]? { get set }
```

```objc
@property (copy, nullable) NSArray * values;
```

## Discussion

The keyframe values represent the values through which the animation must proceed. The time at which a given keyframe value is applied to the layer depends on the animation timing, which is controlled by the [`calculationMode`](./calculationmode.md), [`keyTimes`](./keytimes.md), and [`timingFunctions`](./timingfunctions.md) properties. Values between keyframes are created using interpolation, unless the calculation mode is set to [`discrete`](../caanimationcalculationmode/discrete.md).

Depending on the type of the property, you may need to wrap the values in this array with an [`NSNumber`](../../Foundation/nsnumber.md) of [`NSValue`](../../Foundation/nsvalue.md) object. For some Core Graphics data types, you may also need to cast them to `id` before adding them to the array.

The values in this property are used only if the value in the [`path`](./path.md) property is `nil`.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Providing keyframe values
- [var path: CGPath?](./path.md)
  The path for a point-based property to follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/values)*