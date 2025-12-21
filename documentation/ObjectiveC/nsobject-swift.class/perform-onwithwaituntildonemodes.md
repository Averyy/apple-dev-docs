# perform(_:on:with:waitUntilDone:modes:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invokes a method of the receiver on the specified thread using the specified modes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)
```

#### Discussion

You can use this method to deliver messages to other threads in your application. The message in this case is a method of the current object that you want to execute on the target thread.

This method queues the message on the run loop of the target thread using the run loop modes specified in the `array` parameter. As part of its normal run loop processing, the target thread dequeues the message (assuming it is running in one of the specified modes) and invokes the desired method.

You cannot cancel messages queued using this method. If you want the option of canceling a message on the current thread, you must use either the [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md) or [`perform(_:with:afterDelay:inModes:)`](nsobject-swift.class/perform(_:with:afterdelay:inmodes:).md) method instead.

##### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [`dispatch_after`](https://developer.apple.com/documentation/Dispatch/dispatch_after) and related methods to get the behavior you want.

## Parameters

- `aSelector`: A   that identifies the method to invoke. It should not have a significant return value and should take a single argument of type id, or no arguments.
- `thr`: The thread on which to execute  . This thread represents the target thread.
- `arg`: The argument to pass to the method when it is invoked. Pass   if the method does not take an argument.
- `wait`: If the current thread and target thread are the same, and you specify   for this parameter, the selector is performed immediately. If you specify  , this method queues the message and returns immediately, regardless of whether the threads are the same or different.
- `array`: An array of strings that identifies the modes in which it is permissible to perform the specified selector. This array must contain at least one string. If you specify   or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see   in  .

## See Also

- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](nsobject-swift.class/perform(_:with:afterdelay:).md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval, inModes: [RunLoop.Mode])](nsobject-swift.class/perform(_:with:afterdelay:inmodes:).md)
  Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](nsobject-swift.class/performselector(onmainthread:with:waituntildone:).md)
  Invokes a method of the receiver on the main thread using the default mode.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool, modes: [String]?)](nsobject-swift.class/performselector(onmainthread:with:waituntildone:modes:).md)
  Invokes a method of the receiver on the main thread using the specified modes.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool)](nsobject-swift.class/perform(_:on:with:waituntildone:).md)
  Invokes a method of the receiver on the specified thread using the default mode.
- [func performSelector(inBackground: Selector, with: Any?)](nsobject-swift.class/performselector(inbackground:with:).md)
  Invokes a method of the receiver on a new background thread.
- [class func cancelPreviousPerformRequests(withTarget: Any)](nsobject-swift.class/cancelpreviousperformrequests(withtarget:).md)
  Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md) instance method.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:).md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:on:with:waituntildone:modes:))*