# CFRunLoopGetMain()

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the main CFRunLoop object.

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
func CFRunLoopGetMain() -> CFRunLoop!
```

```c
extern CFRunLoopRefCFRunLoopGetMain();
```

## Return Value

The main run loop. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Getting a Run Loop
- [func CFRunLoopGetCurrent() -> CFRunLoop!](./cfrunloopgetcurrent%28%29.md)
  Returns the CFRunLoop object for the current thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopgetmain())*