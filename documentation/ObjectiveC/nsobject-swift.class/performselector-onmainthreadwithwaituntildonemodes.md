# performSelector(onMainThread:with:waitUntilDone:modes:)

**Framework**: Objective-C Runtime  
**Kind**: method

Invokes a method of the receiver on the main thread using the specified modes.

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
func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)
```

#### Discussion

You can use this method to deliver messages to the main thread of your application. The main thread encompasses the application’s main run loop, and is where the `NSApplication` object receives events. The message in this case is a method of the current object that you want to execute on the thread.

This method queues the message on the run loop of the main thread using the run loop modes specified in the `array` parameter. As part of its normal run loop processing, the main thread dequeues the message (assuming it is running in one of the specified modes) and invokes the desired method. Multiple calls to this method from the same thread cause the corresponding selectors to be queued and performed in the same same order in which the calls were made, assuming the associated run loop modes for each selector are the same. If you specify different modes for each selector, any selectors whose associated mode does not match the current run loop mode are skipped until the run loop subsequently executes in that mode.

You cannot cancel messages queued using this method. If you want the option of canceling a message on the current thread, you must use either the [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md) or [`perform(_:with:afterDelay:inModes:)`](nsobject-swift.class/perform(_:with:afterdelay:inmodes:).md) method.

##### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [`dispatch_after`](https://developer.apple.com/documentation/Dispatch/dispatch_after) and related methods to get the behavior you want.

## Parameters

- `aSelector`: A   that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.
- `arg`: The argument to pass to the method when it is invoked. Pass   if the method does not take an argument.
- `wait`: If the current thread is also the main thread, and you pass  , the message is performed immediately, otherwise the perform is queued to run the next time through the run loop.
- `array`: An array of strings that identifies the modes in which it is permissible to perform the specified selector. This array must contain at least one string. If you specify   or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see   in  .

## See Also

- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](nsobject-swift.class/perform(_:with:afterdelay:).md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval, inModes: [RunLoop.Mode])](nsobject-swift.class/perform(_:with:afterdelay:inmodes:).md)
  Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](nsobject-swift.class/performselector(onmainthread:with:waituntildone:).md)
  Invokes a method of the receiver on the main thread using the default mode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performselector(onmainthread:with:waituntildone:modes:))*