# canSpawnSeparateThread

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the print operation is allowed to spawn a separate printing thread.

**Availability**:
- macOS

## Declaration

```swift
var canSpawnSeparateThread: Bool { get set }
```

```objc
@property BOOL canSpawnSeparateThread;
```

## Discussion

If `canSpawnSeparateThread` is [`true`](../../Swift/true.md), an `NSThread` object is detached when the print panel is dismissed (or immediately, if the panel is not to be displayed). The new thread performs the print operation, so that control can return to your application. A thread is detached only if the print operation is run using the [`runModal(for:delegate:didRun:contextInfo:)`](./runmodal%28for,delegate,didrun,contextinfo%29.md) method. If `canSpawnSeparateThread` is [`false`](../../Swift/false.md), the operation runs on the current thread, blocking the application until the operation completes.

If you send [`canSpawnSeparateThread`](./canspawnseparatethread.md) to an `NSPrintOperation` object with an argument of [`true`](../../Swift/true.md), then the delegate specified in a subsequent invocation of [`runModal(for:delegate:didRun:contextInfo:)`](./runmodal%28for,delegate,didrun,contextinfo%29.md) may be messaged in that spawned, non-main thread.

## Parameters

- `canSpawnSeparateThread`: [`true`](../../Swift/true.md) if the receiver is allowed to spawn a separate thread; otherwise, [`false`](../../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/canspawnseparatethread)*