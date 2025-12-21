# deliverResult()

**Framework**: AppKit  
**Kind**: method

Delivers the results of the print operation to the intended destination.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deliverResult() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the results were successfully delivered; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method may be called to deliver the results to the printer spool or preview application.  Do not invoke this method directly—it is invoked automatically when the print operation is done.

## See Also

- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func cleanUp()](nsprintoperation/cleanup.md)
  Called at the end of a print operation to remove the print operation as the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/deliverresult())*