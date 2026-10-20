# scheduleAutosaving()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Schedules periodic autosaving for the purpose of crash protection.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func scheduleAutosaving()
```

```objc
- (void) scheduleAutosaving;
```

#### Discussion

The default implementation of this method checks to see if autosaving is turned on and, if so and if `[self hasUnautosavedChanges]` returns [`true`](../../Swift/true.md), schedules an `NSTimer` to invoke [`autosave(withDelegate:didAutosave:contextInfo:)`](./autosave%28withdelegate,didautosave,contextinfo%29.md) in the future. If `[self hasUnautosavedChanges]` returns [`false`](../../Swift/false.md) it unschedules any previously scheduled timer. It takes care not to cause [`autosave(withDelegate:didAutosave:contextInfo:)`](./autosave%28withdelegate,didautosave,contextinfo%29.md) to be invoked before a previous invocation caused by it has finished. The exact timings it uses are complicated and subject to change in future releases of macOS. You can override this method to control when exactly periodic autosaving happens. It is invoked by [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) and [`updateChangeCount(withToken:for:)`](./updatechangecount%28withtoken,for%29.md).

## See Also

### Autosaving the Document
- [func checkAutosavingSafety() throws](./checkautosavingsafety%28%29.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [var hasUnautosavedChanges: Bool](./hasunautosavedchanges.md)
  A Boolean value that indicates whether the document has changes that have not been autosaved.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](./autosave%28withdelegate,didautosave,contextinfo%29.md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](./autosave%28withimplicitcancellability,completionhandler%29.md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.
- [var backupFileURL: URL?](./backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/scheduleautosaving())*