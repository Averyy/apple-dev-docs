# performSelector(inBackground:with:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Invokes a method of the receiver on a new background thread.

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
func performSelector(inBackground aSelector: Selector, with arg: Any?)
```

```objc
- (void) performSelectorInBackground:(SEL) aSelector withObject:(id) arg;
```

#### Discussion

This method creates a new thread in your application, putting your application into multithreaded mode if it was not already. The method represented by `aSelector` must set up the thread environment just as you would for any other new thread in your program. For more information about how to configure and run threads, see [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## Parameters

- `aSelector`: A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.
- `arg`: The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

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
- [class func cancelPreviousPerformRequests(withTarget: Any)](./cancelpreviousperformrequests%28withtarget%29.md)
  Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md) instance method.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](./cancelpreviousperformrequests%28withtarget,selector,object%29.md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](./perform%28_,with,afterdelay%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performselector(inbackground:with:))*