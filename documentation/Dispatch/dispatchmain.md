# dispatchMain()

**Framework**: Dispatch  
**Kind**: func

Executes blocks submitted to the main queue.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func dispatchMain() -> Never
```

#### Discussion

This function “parks” the main thread and waits for blocks to be submitted to the main queue. Applications that call [`UIApplicationMain(_:_:_:_:)`](https://developer.apple.com/documentation/UIKit/UIApplicationMain(_:_:_:_:)-1yub7) (iOS), [`NSApplicationMain(_:_:)`](https://developer.apple.com/documentation/AppKit/NSApplicationMain(_:_:)) (macOS), or [`CFRunLoopRun()`](https://developer.apple.com/documentation/CoreFoundation/CFRunLoopRun()) on the main thread must not call [`dispatchMain()`](dispatchmain().md).

This function never returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchmain())*