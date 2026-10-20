# perform(_:with:afterDelay:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invokes a method of the receiver on the current thread using the default mode after a delay.

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
func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)
```

```objc
- (void) performSelector:(SEL) aSelector withObject:(id) anArgument afterDelay:(NSTimeInterval) delay;
```

#### Discussion

This method sets up a timer to perform the `aSelector` message on the current thread’s run loop. The timer is configured to run in the default mode (`NSDefaultRunLoopMode`). When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in the default mode; otherwise, the timer waits until the run loop is in the default mode.

If you want the message to be dequeued when the run loop is in a mode other than the default mode, use the [`perform(_:with:afterDelay:inModes:)`](./perform%28_,with,afterdelay,inmodes%29.md) method instead. If you are not sure whether the current thread is the main thread, you can use the [`performSelector(onMainThread:with:waitUntilDone:)`](./performselector%28onmainthread,with,waituntildone%29.md) or [`performSelector(onMainThread:with:waitUntilDone:modes:)`](./performselector%28onmainthread,with,waituntildone,modes%29.md) method to guarantee that your selector executes on the main thread. To cancel a queued message, use the [`cancelPreviousPerformRequests(withTarget:)`](./cancelpreviousperformrequests%28withtarget%29.md) or [`cancelPreviousPerformRequests(withTarget:selector:object:)`](./cancelpreviousperformrequests%28withtarget,selector,object%29.md) method.

##### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [`dispatch_after`](../../Dispatch/dispatch_after.md) and related methods to get the behavior you want.

## Parameters

- `aSelector`: A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.
- `anArgument`: The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.
- `delay`: The minimum time before which the message is sent. Specifying a delay of 0 does not necessarily cause the selector to be performed immediately. The selector is still queued on the thread’s run loop and performed as soon as possible.

## See Also

### Sending Messages
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
- [class func cancelPreviousPerformRequests(withTarget: Any)](./cancelpreviousperformrequests%28withtarget%29.md)
  Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md) instance method.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](./cancelpreviousperformrequests%28withtarget,selector,object%29.md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:))*