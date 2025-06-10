# CFRunLoopPerformBlock(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Enqueues a block object on a given runloop to be executed as the runloop cycles in specified modes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFRunLoopPerformBlock(_ rl: CFRunLoop!, _ mode: CFTypeRef!, _ block: (() -> Void)!)
```

#### Discussion

When the runloop runs in the specified `mode`, the block object is executed. You can use this function as a means to offload work to another thread similar to Cocoa’s doc://com.apple.documentation/documentation/objectivec/nsobject/1414476-perform and related methods. You can also use it as an alternative to mechanisms such as putting a CFRunLoopTimer in the other thread’s run loop, or using CFMessagePort to pass information between threads.

This method enqueues the block only and does not automatically wake up the specified run loop. Therefore, execution of the block occurs the next time the run loop wakes up to handle another input source. If you want the work performed right away, you must explicitly wake up that thread using the [`CFRunLoopWakeUp(_:)`](cfrunloopwakeup(_:).md) function.

## Parameters

- `rl`: A run loop.
- `mode`: A CFString that identifies a runloop mode, or a CFArray of CFStrings that each identify a runloop mode.
- `block`: The block is copied by the function before the function returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopperformblock(_:_:_:))*