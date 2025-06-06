# CAMetalDisplayLink.Update

**Framework**: Core Animation  
**Kind**: class

Stores information about a single update from a Metal display link instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class Update
```

## Topics

### Timing the Next Animation Frame
- [var targetPresentationTimestamp: CFTimeInterval](cametaldisplaylink/update/targetpresentationtimestamp.md)
  The time the system estimates until the display of the next frame.
- [var targetPresentationTimestamp: CFTimeInterval](cametaldisplaylink/update/targetpresentationtimestamp.md)
  The time the system estimates until the display of the next frame.
### Drawing the Next Frame
- [var targetTimestamp: CFTimeInterval](cametaldisplaylink/update/targettimestamp.md)
  A deadline that indicates when your app needs to finish rendering to the drawable.
- [var drawable: any CAMetalDrawable](cametaldisplaylink/update/drawable.md)
  The Metal drawable your app uses to render the next frame.
- [var targetTimestamp: CFTimeInterval](cametaldisplaylink/update/targettimestamp.md)
  A deadline that indicates when your app needs to finish rendering to the drawable.
- [var drawable: any CAMetalDrawable](cametaldisplaylink/update/drawable.md)
  The Metal drawable your app uses to render the next frame.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func CACurrentMediaTime() -> CFTimeInterval](cacurrentmediatime().md)
  Returns the current absolute time, in seconds.
- [class CAMediaTimingFunction](camediatimingfunction.md)
  A function that defines the pacing of an animation as a timing curve.
- [protocol CAMediaTiming](camediatiming.md)
  Methods that model a hierarchical timing system, allowing objects to map time between their parent and local time.
- [class CADisplayLink](cadisplaylink.md)
  A timer object that allows your app to synchronize its drawing to the refresh rate of the display.
- [class CAMetalDisplayLink](cametaldisplaylink.md)
  A class your Metal app uses to register for callbacks to synchronize its animations for a display.
- [protocol CAMetalDisplayLinkDelegate](cametaldisplaylinkdelegate.md)
  A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylink/update)*