# run()

**Framework**: AppKit  
**Kind**: method

Runs the print operation on the current thread.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func run() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the operation was successful; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The operation runs to completion in the current thread, blocking the application. A separate thread is not spawned, even if [`canSpawnSeparateThread`](nsprintoperation/canspawnseparatethread.md) is [`true`](https://developer.apple.com/documentation/swift/true). Use [`runModal(for:delegate:didRun:contextInfo:)`](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md) to use document-modal sheets and to allow a separate thread to perform the operation.

## See Also

- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func cleanUp()](nsprintoperation/cleanup.md)
  Called at the end of a print operation to remove the print operation as the current operation.
- [func deliverResult() -> Bool](nsprintoperation/deliverresult.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/run())*