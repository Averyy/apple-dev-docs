# runModal(for:delegate:didRun:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Runs the print operation, calling your custom delegate method upon completion.

**Availability**:
- macOS

## Declaration

```swift
func runModal(for docWindow: NSWindow, delegate: Any?, didRun didRunSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) runOperationModalForWindow:(NSWindow *) docWindow delegate:(id) delegate didRunSelector:(SEL) didRunSelector contextInfo:(void *) contextInfo;
```

#### Discussion

The method specified by the  `didRunSelector` parameter must have the following signature:

```objc
- (void)printOperationDidRun:(NSPrintOperation *)printOperation  success:(BOOL)success  contextInfo:(void *)contextInfo
```

The value of `success` is [`true`](../../Swift/true.md) if the print operation ran to completion without cancellation or error, and [`false`](../../Swift/false.md) otherwise.

If you send [`canSpawnSeparateThread`](./canspawnseparatethread.md) to an `NSPrintOperation` object with an argument of [`true`](../../Swift/true.md), then the delegate specified in a subsequent invocation of [`runModal(for:delegate:didRun:contextInfo:)`](./runmodal%28for,delegate,didrun,contextinfo%29.md) may be messaged in that spawned, non-main thread.

## Parameters

- `docWindow`: The document window to receive a print progress sheet.
- `delegate`: The printing delegate object. Messages are sent to this object.
- `didRunSelector`: The delegate method called after the completion of the print operation.
- `contextInfo`: A pointer to any data you want passed to the method in the  `didRunSelector` parameter.

## See Also

### Running the Print Operation
- [func run() -> Bool](./run%28%29.md)
  Runs the print operation on the current thread.
- [func cleanUp()](./cleanup%28%29.md)
  Called at the end of a print operation to remove the print operation as the current operation.
- [func deliverResult() -> Bool](./deliverresult%28%29.md)
  Delivers the results of the print operation to the intended destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintoperation/runmodal(for:delegate:didrun:contextinfo:))*