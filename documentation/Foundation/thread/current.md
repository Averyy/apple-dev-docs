# current

**Framework**: Foundation  
**Kind**: property

Returns the thread object representing the current thread of execution.

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
class var current: Thread { get }
```

#### Return Value

A thread object representing the current thread of execution.

## See Also

- [class func detachNewThreadSelector(Selector, toTarget: Any, with: Any?)](thread/detachnewthreadselector(_:totarget:with:).md)
  Detaches a new thread and uses the specified selector as the thread entry point.
- [class func isMultiThreaded() -> Bool](thread/ismultithreaded.md)
  Returns whether the application is multithreaded.
- [class var callStackReturnAddresses: [NSNumber]](thread/callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.
- [class var callStackSymbols: [String]](thread/callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/current)*