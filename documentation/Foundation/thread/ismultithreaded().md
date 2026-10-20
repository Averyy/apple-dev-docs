# isMultiThreaded()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (BOOL) isMultiThreaded;
```

#### Return Value

[`true`](../../Swift/true.md) if the application is multithreaded, otherwise [`false`](../../Swift/false.md).

#### Discussion

An application is considered multithreaded if a thread was ever detached from the main thread using either [`detachNewThreadSelector(_:toTarget:with:)`](./detachnewthreadselector%28_,totarget,with%29.md) or [`start()`](./start%28%29.md). If you detached a thread in your application using a non-Cocoa API, such as the POSIX or Multiprocessing Services APIs, this method could still return [`false`](../../Swift/false.md). The detached thread does not have to be currently running for the application to be considered multithreaded—this method only indicates whether a single thread has been spawned.

## See Also

### Querying the Environment
- [class var current: Thread](./current.md)
  Returns the thread object representing the current thread of execution.
- [class var callStackReturnAddresses: [NSNumber]](./callstackreturnaddresses.md)
  Returns an array containing the call stack return addresses.
- [class var callStackSymbols: [String]](./callstacksymbols.md)
  Returns an array containing the call stack symbols.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/thread/ismultithreaded())*