# timingFunctions

**Framework**: Core Animation  
**Kind**: property

An optional array of `CAMediaTimingFunction` objects that define the pacing for each keyframe segment.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timingFunctions: [CAMediaTimingFunction]? { get set }
```

#### Discussion

You can use this array to apply ease-in, ease-out, or custom timing curves to the points that lie between two keyframe values. If the number of keyframes in the values property is , then this property should contain `-1` objects.

If you provide timing information in the [`keyTimes`](cakeyframeanimation/keytimes.md) property, the timing functions you specify using this property further modify the timing between those values. If you do not assign a value to the [`keyTimes`](cakeyframeanimation/keytimes.md) property, the timing functions modify the default timing provided by the animation object.

If you also specify a timing function in the animation object’s [`timingFunction`](caanimation/timingfunction.md) property, that function is applied first followed by the timing function for the specific keyframe segment.

For information on how to create a timing function, see [`CAMediaTimingFunction`](camediatimingfunction.md).

## See Also

- [var keyTimes: [NSNumber]?](cakeyframeanimation/keytimes.md)
  An optional array of `NSNumber` objects that define the time at which to apply a given keyframe segment.
- [var calculationMode: CAAnimationCalculationMode](cakeyframeanimation/calculationmode.md)
  Specifies how intermediate keyframe values are calculated by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/timingfunctions)*