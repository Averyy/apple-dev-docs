# CFRunLoopGetCurrent()

**Framework**: Core Foundation  
**Kind**: func

Returns the CFRunLoop object for the current thread.

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
func CFRunLoopGetCurrent() -> CFRunLoop!
```

#### Return Value

Current thread’s run loop. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

Each thread has exactly one run loop associated with it.

## See Also

- [Threading Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)
- [Concurrency Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ConcurrencyProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40008091)
- [func CFRunLoopGetMain() -> CFRunLoop!](cfrunloopgetmain().md)
  Returns the main CFRunLoop object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopgetcurrent())*