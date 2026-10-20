# run()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the print operation on the current thread.

**Availability**:
- macOS

## Declaration

```swift
func run() -> Bool
```

```objc
- (BOOL) runOperation;
```

#### Return Value

[`true`](../../Swift/true.md) if the operation was successful; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The operation runs to completion in the current thread, blocking the application. A separate thread is not spawned, even if [`canSpawnSeparateThread`](./canspawnseparatethread.md) is [`true`](../../Swift/true.md). Use [`runModal(for:delegate:didRun:contextInfo:)`](./runmodal%28for,delegate,didrun,contextinfo%29.md) to use document-modal sheets and to allow a separate thread to perform the operation.

## See Also

### Running the Print Operation
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodal%28for,delegate,didrun,contextinfo%29.md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func cleanUp()](./cleanup%28%29.md)
  Called at the end of a print operation to remove the print operation as the current operation.
- [func deliverResult() -> Bool](./deliverresult%28%29.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/run())*