# performSelector(onMainThread:with:waitUntilDone:modes:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invokes a method of the receiver on the main thread using the specified modes.

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
func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)
```

```objc
- (void) performSelectorOnMainThread:(SEL) aSelector withObject:(id) arg waitUntilDone:(BOOL) wait modes:(NSArray<NSString *> *) array;
```

#### Discussion

You can use this method to deliver messages to the main thread of your application. The main thread encompasses the application’s main run loop, and is where the `NSApplication` object receives events. The message in this case is a method of the current object that you want to execute on the thread.

This method queues the message on the run loop of the main thread using the run loop modes specified in the `array` parameter. As part of its normal run loop processing, the main thread dequeues the message (assuming it is running in one of the specified modes) and invokes the desired method. Multiple calls to this method from the same thread cause the corresponding selectors to be queued and performed in the same same order in which the calls were made, assuming the associated run loop modes for each selector are the same. If you specify different modes for each selector, any selectors whose associated mode does not match the current run loop mode are skipped until the run loop subsequently executes in that mode.

You cannot cancel messages queued using this method. If you want the option of canceling a message on the current thread, you must use either the [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md) or [`perform(_:with:afterDelay:inModes:)`](./perform%28_,with,afterdelay,inmodes%29.md) method.

##### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [`dispatch_after`](../../Dispatch/dispatch_after.md) and related methods to get the behavior you want.

## Parameters

- `aSelector`: A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.
- `arg`: The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.
- `wait`: A Boolean that specifies whether the current thread blocks until after the specified selector is performed on the receiver on the main thread. Specify [`YES`](../yes.md) to block this thread; otherwise, specify [`NO`](../no.md) to have this method return immediately.

  If the current thread is also the main thread, and you pass [`YES`](../yes.md), the message is performed immediately, otherwise the perform is queued to run the next time through the run loop.
- `array`: An array of strings that identifies the modes in which it is permissible to perform the specified selector. This array must contain at least one string. If you specify `nil` or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see [Run Loops](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16) in [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## See Also

### Sending Messages
- [func perform(Selector, with: Any?, afterDelay: TimeInterval)](./perform%28_,with,afterdelay%29.md)
  Invokes a method of the receiver on the current thread using the default mode after a delay.
- [func perform(Selector, with: Any?, afterDelay: TimeInterval, inModes: [RunLoop.Mode])](./perform%28_,with,afterdelay,inmodes%29.md)
  Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [func performSelector(onMainThread: Selector, with: Any?, waitUntilDone: Bool)](./performselector%28onmainthread,with,waituntildone%29.md)
  Invokes a method of the receiver on the main thread using the default mode.
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

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performselector(onmainthread:with:waituntildone:modes:))*