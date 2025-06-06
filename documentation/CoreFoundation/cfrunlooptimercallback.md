# CFRunLoopTimerCallBack

**Framework**: Core Foundation  
**Kind**: typealias

Callback invoked when a CFRunLoopTimer object fires.

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
typealias CFRunLoopTimerCallBack = (CFRunLoopTimer?, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

If `timer` repeats, the run loop automatically schedules the next firing time after calling this function, unless you manually update the firing time within this callback by calling [`CFRunLoopTimerSetNextFireDate(_:_:)`](cfrunlooptimersetnextfiredate(_:_:).md). If `timer` does not repeat, the run loop invalidates `timer`.

You specify this callback when you create the timer with [`CFRunLoopTimerCreate(_:_:_:_:_:_:_:)`](cfrunlooptimercreate(_:_:_:_:_:_:_:).md).

## Parameters

- `timer`: The run loop timer that is firing.
- `info`: The   member of the   structure that was used when creating the run loop timer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercallback)*