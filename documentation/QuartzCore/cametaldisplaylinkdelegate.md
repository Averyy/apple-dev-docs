# CAMetalDisplayLinkDelegate

**Framework**: Core Animation  
**Kind**: protocol

A protocol your app implements to respond to callbacks from Core Animation for a Metal display link.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
protocol CAMetalDisplayLinkDelegate
```

#### Overview

Your app responds to the system on behalf of a [`CAMetalDisplayLink`](cametaldisplaylink.md) with this protocol. Implement a type that adopts the protocol and assign an instance of it to a display link’s [`delegate`](cametaldisplaylink/delegate.md) property.

## Topics

### Receiving Display Updates
- [func metalDisplayLink(CAMetalDisplayLink, needsUpdate: CAMetalDisplayLink.Update)](cametaldisplaylinkdelegate/metaldisplaylink(_:needsupdate:).md)
  A method the system calls to notify your app when it plans to update the display.

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
- [CAMetalDisplayLink.Update](cametaldisplaylink/update.md)
  Stores information about a single update from a Metal display link instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldisplaylinkdelegate)*