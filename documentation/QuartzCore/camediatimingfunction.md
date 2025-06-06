# CAMediaTimingFunction

**Framework**: Core Animation  
**Kind**: class

A function that defines the pacing of an animation as a timing curve.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class CAMediaTimingFunction
```

#### Overview

`CAMediaTimingFunction` represents one segment of a function that defines the pacing of an animation as a timing curve. The function maps an input time normalized to the range `[0,1]` to an output time also in the range `[0,1]`.

You can create a media timing function by supplying your own cubic Bézier curve control points using the [`init(controlPoints:_:_:_:)`](camediatimingfunction/init(controlpoints:_:_:_:).md) method or by using one of the predefined timing functions.

## Topics

### Creating Timing Functions
- [convenience init(name: CAMediaTimingFunctionName)](camediatimingfunction/init(name:).md)
  Creates and returns a new instance of `CAMediaTimingFunction` configured with the predefined timing function specified by `name`.
- [init(controlPoints: Float, Float, Float, Float)](camediatimingfunction/init(controlpoints:_:_:_:).md)
  Returns an initialized timing function modeled as a cubic Bézier curve using the specified control points.
### Accessing the Control Points
- [func getControlPoint(at: Int, values: UnsafeMutablePointer<Float>)](camediatimingfunction/getcontrolpoint(at:values:).md)
  Returns the control point for the specified index.
### Constants
- [Predefined Timing Functions](predefined-timing-functions.md)
  Constants that specify system-provided timing functions, used by [`init(name:)`](camediatimingfunction/init(name:).md).

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func CACurrentMediaTime() -> CFTimeInterval](cacurrentmediatime().md)
  Returns the current absolute time, in seconds.
- [protocol CAMediaTiming](camediatiming.md)
  Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [class CADisplayLink](cadisplaylink.md)
  A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunction)*