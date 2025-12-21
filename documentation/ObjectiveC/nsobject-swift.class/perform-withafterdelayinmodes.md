# perform(_:with:afterDelay:inModes:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invokes a method of the receiver on the current thread using the specified modes after a delay.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoop.Mode])
```

#### Discussion

This method sets up a timer to perform the `aSelector` message on the current thread’s run loop. The timer is configured to run in the modes specified by the `modes` parameter. When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in one of the specified modes; otherwise, the timer waits until the run loop is in one of those modes.

If you want the message to be dequeued when the run loop is in a mode other than the default mode, use the [`perform(_:with:afterDelay:inModes:)`](nsobject-swift.class/perform(_:with:afterdelay:inmodes:).md) method instead. If you are not sure whether the current thread is the main thread, you can use the [`performSelector(onMainThread:with:waitUntilDone:)`](nsobject-swift.class/performselector(onmainthread:with:waituntildone:).md) or [`performSelector(onMainThread:with:waitUntilDone:modes:)`](nsobject-swift.class/performselector(onmainthread:with:waituntildone:modes:).md) method to guarantee that your selector executes on the main thread. To cancel a queued message, use the [`cancelPreviousPerformRequests(withTarget:)`](nsobject-swift.class/cancelpreviousperformrequests(withtarget:).md) or [`cancelPreviousPerformRequests(withTarget:selector:object:)`](nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:).md) method.

##### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [`dispatch_after`](https://developer.apple.com/documentation/Dispatch/dispatch_after) and related methods to get the behavior you want.

## Parameters

- `aSelector`: A   that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.
- `anArgument`: The argument to pass to the method when it is invoked. Pass   if the method does not take an argument.
- `delay`: The minimum time before which the message is sent. Specifying a delay of 0 does not necessarily cause the selector to be performed immediately. The selector is still queued on the thread’s run loop and performed as soon as possible.
- `modes`: An array of strings that identify the modes to associate with the timer that performs the selector. This array must contain at least one string. If you specify   or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see   in  .

## See Also

- [func invalidate()](../Foundation/Timer/invalidate.md)
  Stops the timer from ever firing again and requests its removal from its run loop.
- [func add(Timer, forMode: RunLoop.Mode)](../Foundation/RunLoop/add(_:forMode:)-392ag.md)
  Registers a given timer with a given input mode.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](nsobject-swift.class/perform(_:with:afterdelay:).md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](nsobject-swift.class/performselector(onmainthread:with:waituntildone:).md)
  Invokes a method of the receiver on the main thread using the default mode.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool, modes: [String]?)](nsobject-swift.class/performselector(onmainthread:with:waituntildone:modes:).md)
  Invokes a method of the receiver on the main thread using the specified modes.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool)](nsobject-swift.class/perform(_:on:with:waituntildone:).md)
  Invokes a method of the receiver on the specified thread using the default mode.
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool, modes: [String]?)](nsobject-swift.class/perform(_:on:with:waituntildone:modes:).md)
  Invokes a method of the receiver on the specified thread using the specified modes.
- [func performSelector(inBackground: Selector, with: Any?)](nsobject-swift.class/performselector(inbackground:with:).md)
  Invokes a method of the receiver on a new background thread.
- [class func cancelPreviousPerformRequests(withTarget: Any)](nsobject-swift.class/cancelpreviousperformrequests(withtarget:).md)
  Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md) instance method.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:).md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:inmodes:))*