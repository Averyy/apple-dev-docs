# UICubicTimingParameters

**Framework**: UIKit  
**Kind**: class

The timing information for animations in the form of a cubic Bézier curve.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICubicTimingParameters
```

#### Overview

Use a [`UICubicTimingParameters`](uicubictimingparameters.md) object to specify custom timing curves when creating animations with objects that adopt the [`UIViewAnimating`](uiviewanimating.md) protocol, such as [`UIViewPropertyAnimator`](uiviewpropertyanimator.md).

A cubic Bézier timing curve consists of a line whose starting point is (`0`, `0`), whose end point is (`1`, `1`), and whose shape is defined by two control points. The slope of the line at each point in time defines the speed of the animation at that time. Steep slopes cause animations to appear to run faster and shallower slopes cause them to appear to run slower. The following graph shows a timing curve where the animations start fast and finish fast but run more slowly through the middle section.

![A graph that shows a cubic Bézier timing curve.](https://docs-assets.developer.apple.com/published/0054ab7fbcfb5dc1810282e7c7d2a202/media-1965827%402x.png)

## Topics

### Initializing a cubic timing parameters object
- [init()](uicubictimingparameters/init.md)
  Initializes the object with the system’s default timing curve.
- [init(animationCurve: UIView.AnimationCurve)](uicubictimingparameters/init(animationcurve:).md)
  Initializes the object with the specified UIKit timing curve.
- [init(controlPoint1: CGPoint, controlPoint2: CGPoint)](uicubictimingparameters/init(controlpoint1:controlpoint2:).md)
  Initializes the object with the specified control points for a cubic Bézier curve.
- [init?(coder: NSCoder)](uicubictimingparameters/init(coder:).md)
  Creates a timing parameters object from data in an unarchiver.
### Getting the timing parameters
- [var animationCurve: UIView.AnimationCurve](uicubictimingparameters/animationcurve.md)
  The standard UIKit animation curve to use for timing.
- [var controlPoint1: CGPoint](uicubictimingparameters/controlpoint1.md)
  The first control point for the cubic Bézier curve.
- [var controlPoint2: CGPoint](uicubictimingparameters/controlpoint2.md)
  The second control point of the cubic Bézier curve.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UITimingCurveProvider](uitimingcurveprovider.md)

## See Also

- [protocol UITimingCurveProvider](uitimingcurveprovider.md)
  An interface for providing the timing information needed to perform animations.
- [class UISpringTimingParameters](uispringtimingparameters.md)
  The timing information for animations that mimics the behavior of a spring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicubictimingparameters)*