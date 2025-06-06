# CFRunLoopGetMain()

**Framework**: Core Foundation  
**Kind**: func

Returns the main CFRunLoop object.

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
func CFRunLoopGetMain() -> CFRunLoop!
```

#### Return Value

The main run loop. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

- [func CFRunLoopGetCurrent() -> CFRunLoop!](cfrunloopgetcurrent().md)
  Returns the CFRunLoop object for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopgetmain())*