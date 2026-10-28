# distantFuture

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

```objc
@property (class, copy, readonly) NSDate * distantFuture;
```

## Return Value

An [`NSDate`](../nsdate.md) object representing a date in the distant future (in terms of centuries).

## Discussion

You can pass this value when an [`NSDate`](../nsdate.md) object is required to have the date argument essentially ignored. For example, the [`NSWindow`](../../AppKit/nswindow.md) method [`nextEvent(matching:until:inMode:dequeue:)`](../../AppKit/nswindow/nextevent%28matching,until,inmode,dequeue%29.md) returns `nil` if an event specified in the event mask does not happen before the specified date. You can use the object returned by [`distantFuture`](./distantfuture.md) as the date argument to wait indefinitely for the event to occur.

```objc
myEvent = [myWindow nextEventMatchingMask:myEventMask
    untilDate:[NSDate distantFuture]
    inMode:NSDefaultRunLoopMode
    dequeue:YES];
```

## See Also

### Getting Temporal Boundaries
- [class var distantPast: Date](./distantpast.md)
  A date object representing a date in the distant past.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdate/distantfuture)*