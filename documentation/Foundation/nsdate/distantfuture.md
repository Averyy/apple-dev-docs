# distantFuture

**Framework**: Foundation  
**Kind**: property

A date object representing a date in the distant future.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class var distantFuture: Date { get }
```

#### Return Value

An [`NSDate`](nsdate.md) object representing a date in the distant future (in terms of centuries).

#### Discussion

You can pass this value when an [`NSDate`](nsdate.md) object is required to have the date argument essentially ignored. For example, the [`NSWindow`](https://developer.apple.com/documentation/AppKit/NSWindow) method [`nextEvent(matching:until:inMode:dequeue:)`](https://developer.apple.com/documentation/AppKit/NSWindow/nextEvent(matching:until:inMode:dequeue:)) returns `nil` if an event specified in the event mask does not happen before the specified date. You can use the object returned by [`distantFuture`](nsdate/distantfuture.md) as the date argument to wait indefinitely for the event to occur.

```objc
myEvent = [myWindow nextEventMatchingMask:myEventMask
    untilDate:[NSDate distantFuture]
    inMode:NSDefaultRunLoopMode
    dequeue:YES];
```

## See Also

- [class var distantPast: Date](nsdate/distantpast.md)
  A date object representing a date in the distant past.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/distantfuture)*