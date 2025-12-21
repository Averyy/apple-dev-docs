# cancelPreviousPerformRequests(withTarget:)

**Framework**: Objective-C Runtime  
**Kind**: method

Cancels perform requests previously registered with the [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md) instance method.

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
class func cancelPreviousPerformRequests(withTarget aTarget: Any)
```

#### Discussion

All perform requests having the same target `aTarget` are canceled. This method removes perform requests only in the current run loop, not all run loops.

## Parameters

- `aTarget`: The target for requests previously registered with the   instance method.

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
- [func perform(Selector, on: Thread, with: Any?, waitUntilDone: Bool, modes: [String]?)](nsobject-swift.class/perform(_:on:with:waituntildone:modes:).md)
  Invokes a method of the receiver on the specified thread using the specified modes.
- [func performSelector(inBackground: Selector, with: Any?)](nsobject-swift.class/performselector(inbackground:with:).md)
  Invokes a method of the receiver on a new background thread.
- [class func cancelPreviousPerformRequests(withTarget: Any, selector: Selector, object: Any?)](nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:).md)
  Cancels perform requests previously registered with [`perform(_:with:afterDelay:)`](nsobject-swift.class/perform(_:with:afterdelay:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:))*