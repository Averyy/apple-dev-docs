# cleanUp()

**Framework**: AppKit  
**Kind**: method

Called at the end of a print operation to remove the print operation as the current operation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func cleanUp()
```

#### Discussion

You typically do not invoke this method directly.

## See Also

- [func run() -> Bool](nsprintoperation/run.md)
  Runs the print operation on the current thread.
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsprintoperation/runmodal(for:delegate:didrun:contextinfo:).md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func deliverResult() -> Bool](nsprintoperation/deliverresult.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/cleanup())*