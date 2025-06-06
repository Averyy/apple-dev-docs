# runModal(for:delegate:didRun:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Runs the print operation, calling your custom delegate method upon completion.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func runModal(for docWindow: NSWindow, delegate: Any?, didRun didRunSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

The method specified by the  `didRunSelector` parameter must have the following signature:

```objc
- (void)printOperationDidRun:(NSPrintOperation *)printOperation  success:(BOOL)success  contextInfo:(void *)contextInfo
```

The value of `success` is [`true`](https://developer.apple.com/documentation/swift/true) if the print operation ran to completion without cancellation or error, and [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

If you send [`canSpawnSeparateThread`](nsprintoperation/canspawnseparatethread.md) to an `NSPrintOperation` object with an argument of [`true`](https://developer.apple.com/documentation/swift/true), then the delegate specified in a subsequent invocation of [`runModal(for:delegate:didRun:contextInfo:)`](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md) may be messaged in that spawned, non-main thread.

## Parameters

- `docWindow`: The document window to receive a print progress sheet.
- `delegate`: The printing delegate object. Messages are sent to this object.
- `didRunSelector`: The delegate method called after the completion of the print operation.
- `contextInfo`: A pointer to any data you want passed to the method in the    parameter.

## See Also

- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [func cleanUp()](nsprintoperation/cleanup.md)
  Called at the end of a print operation to remove the print operation as the current operation.
- [func deliverResult() -> Bool](nsprintoperation/deliverresult.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/runmodal(for:delegate:didrun:contextinfo:))*