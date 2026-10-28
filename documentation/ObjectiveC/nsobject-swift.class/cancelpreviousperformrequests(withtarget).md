# cancelPreviousPerformRequests(withTarget:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md) instance method.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
class func cancelPreviousPerformRequests(withTarget aTarget: Any)
```

```objc
+ (void) cancelPreviousPerformRequestsWithTarget:(id) aTarget;
```

## Discussion

All perform requests having the same target `aTarget` are canceled. This method removes perform requests only in the current run loop, not all run loops.

## Parameters

- `aTarget`: The target for requests previously registered with the [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md) instance method.

## See Also

### Sending Messages
- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](./perform%28_,with,afterdelay%29.md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval, inModes: [RunLoop.Mode])](./perform%28_,with,afterdelay,inmodes%29.md)
  Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](./performselector%28onmainthread,with,waituntildone%29.md)
  Invokes a method of the receiver on the main thread using the default mode.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool, modes: [String]?)](./performselector%28onmainthread,with,waituntildone,modes%29.md)
  Invokes a method of the receiver on the main thread using the specified modes.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool)](./perform%28_,on,with,waituntildone%29.md)
  Invokes a method of the receiver on the specified thread using the default mode.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool, modes: [String]?)](./perform%28_,on,with,waituntildone,modes%29.md)
  Invokes a method of the receiver on the specified thread using the specified modes.
- [func performSelector(inBackground: Selector, with: Any?)](./performselector%28inbackground,with%29.md)
  Invokes a method of the receiver on a new background thread.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](./cancelpreviousperformrequests%28withtarget,selector,object%29.md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:))*