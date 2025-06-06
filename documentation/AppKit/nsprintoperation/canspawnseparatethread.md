# canSpawnSeparateThread

**Framework**: AppKit  
**Kind**: property

A Boolean value that determines whether the print operation is allowed to spawn a separate printing thread.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canSpawnSeparateThread: Bool { get set }
```

#### Discussion

If `canSpawnSeparateThread` is [`true`](https://developer.apple.com/documentation/swift/true), an `NSThread` object is detached when the print panel is dismissed (or immediately, if the panel is not to be displayed). The new thread performs the print operation, so that control can return to your application. A thread is detached only if the print operation is run using the [`runModal(for:delegate:didRun:contextInfo:)`](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md) method. If `canSpawnSeparateThread` is [`false`](https://developer.apple.com/documentation/swift/false), the operation runs on the current thread, blocking the application until the operation completes.

If you send [`canSpawnSeparateThread`](nsprintoperation/canspawnseparatethread.md) to an `NSPrintOperation` object with an argument of [`true`](https://developer.apple.com/documentation/swift/true), then the delegate specified in a subsequent invocation of [`runModal(for:delegate:didRun:contextInfo:)`](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md) may be messaged in that spawned, non-main thread.

## Parameters

- `canSpawnSeparateThread`:   if the receiver is allowed to spawn a separate thread; otherwise,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/canspawnseparatethread)*