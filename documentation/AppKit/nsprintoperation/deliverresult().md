# deliverResult()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Delivers the results of the print operation to the intended destination.

**Availability**:
- macOS

## Declaration

```swift
func deliverResult() -> Bool
```

```objc
- (BOOL) deliverResult;
```

## Return Value

[`true`](../../Swift/true.md) if the results were successfully delivered; otherwise, [`false`](../../Swift/false.md).

## Discussion

This method may be called to deliver the results to the printer spool or preview application.  Do not invoke this method directly—it is invoked automatically when the print operation is done.

## See Also

### Running the Print Operation
- [func run() -> Bool](./run%28%29.md)
  Runs the print operation on the current thread.
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodal%28for,delegate,didrun,contextinfo%29.md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func cleanUp()](./cleanup%28%29.md)
  Called at the end of a print operation to remove the print operation as the current operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/deliverresult())*