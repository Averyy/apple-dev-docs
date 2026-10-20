# dispatchMain()

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Executes blocks submitted to the main queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func dispatchMain() -> Never
```

```c
extern void dispatch_main();
```

#### Discussion

This function “parks” the main thread and waits for blocks to be submitted to the main queue. Applications that call [`UIApplicationMain(_:_:_:_:)`](../UIKit/uiapplicationmain%28_,_,_,_%29-1yub7.md) (iOS), [`NSApplicationMain(_:_:)`](../AppKit/nsapplicationmain%28_,_%29.md) (macOS), or [`CFRunLoopRun()`](../CoreFoundation/cfrunlooprun%28%29.md) on the main thread must not call [`dispatchMain()`](./dispatchmain%28%29.md).

This function never returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchmain())*