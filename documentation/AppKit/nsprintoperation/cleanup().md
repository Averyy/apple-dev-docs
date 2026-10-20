# cleanUp()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called at the end of a print operation to remove the print operation as the current operation.

**Availability**:
- macOS

## Declaration

```swift
func cleanUp()
```

```objc
- (void) cleanUpOperation;
```

#### Discussion

You typically do not invoke this method directly.

## See Also

### Running the Print Operation
- [func run() -> Bool](./run%28%29.md)
  Runs the print operation on the current thread.
- [func runModal(for: NSWindow, delegate: Any?, didRun: Selector?, contextInfo: UnsafeMutableRawPointer?)](./runmodal%28for,delegate,didrun,contextinfo%29.md)
  Runs the print operation, calling your custom delegate method upon completion.
- [func deliverResult() -> Bool](./deliverresult%28%29.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/cleanup())*