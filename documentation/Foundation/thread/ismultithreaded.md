# isMultiThreaded()

**Framework**: Foundation  
**Kind**: method

Returns whether the application is multithreaded.

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
class func isMultiThreaded() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the application is multithreaded, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

An application is considered multithreaded if a thread was ever detached from the main thread using either [`detachNewThreadSelector(_:toTarget:with:)`](thread/detachnewthreadselector(_:totarget:with:).md) or [`start()`](thread/start().md). If you detached a thread in your application using a non-Cocoa API, such as the POSIX or Multiprocessing Services APIs, this method could still return [`false`](https://developer.apple.com/documentation/swift/false). The detached thread does not have to be currently running for the application to be considered multithreaded—this method only indicates whether a single thread has been spawned.

## See Also

- [class var current: Thread](thread/current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackReturnAddresses: [NSNumber]](thread/callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.
- [class var callStackSymbols: [String]](thread/callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/ismultithreaded())*