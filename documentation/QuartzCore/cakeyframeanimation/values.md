# values

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

The keyframe values represent the values through which the animation must proceed. The time at which a given keyframe value is applied to the layer depends on the animation timing, which is controlled by the [`calculationMode`](cakeyframeanimation/calculationmode.md), [`keyTimes`](cakeyframeanimation/keytimes.md), and [`timingFunctions`](cakeyframeanimation/timingfunctions.md) properties. Values between keyframes are created using interpolation, unless the calculation mode is set to [`discrete`](caanimationcalculationmode/discrete.md).

Depending on the type of the property, you may need to wrap the values in this array with an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) of [`NSValue`](https://developer.apple.com/documentation/Foundation/NSValue) object. For some Core Graphics data types, you may also need to cast them to `id` before adding them to the array.

The values in this property are used only if the value in the [`path`](cakeyframeanimation/path.md) property is `nil`.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [var path: CGPath?](cakeyframeanimation/path.md)
  The path for a point-based property to follow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/values)*