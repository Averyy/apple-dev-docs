# scheduleAutosaving()

**Framework**: AppKit  
**Kind**: method

Schedules periodic autosaving for the purpose of crash protection.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func scheduleAutosaving()
```

#### Discussion

The default implementation of this method checks to see if autosaving is turned on and, if so and if `[self hasUnautosavedChanges]` returns [`true`](https://developer.apple.com/documentation/swift/true), schedules an `NSTimer` to invoke [`autosave(withDelegate:didAutosave:contextInfo:)`](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md) in the future. If `[self hasUnautosavedChanges]` returns [`false`](https://developer.apple.com/documentation/swift/false) it unschedules any previously scheduled timer. It takes care not to cause [`autosave(withDelegate:didAutosave:contextInfo:)`](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md) to be invoked before a previous invocation caused by it has finished. The exact timings it uses are complicated and subject to change in future releases of macOS. You can override this method to control when exactly periodic autosaving happens. It is invoked by [`updateChangeCount(_:)`](nsdocument/updatechangecount(_:).md) and [`updateChangeCount(withToken:for:)`](nsdocument/updatechangecount(withtoken:for:).md).

## See Also

- [func checkAutosavingSafety() throws](nsdocument/checkautosavingsafety.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [var hasUnautosavedChanges: Bool](nsdocument/hasunautosavedchanges.md)
  A Boolean value that indicates whether the document has changes that have not been autosaved.
- [func autosave(withDelegate: Any?, didAutosave: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/autosave(withdelegate:didautosave:contextinfo:).md)
  Autosaves the document’s contents to an appropriate location in the file system.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](nsdocument/autosave(withimplicitcancellability:completionhandler:).md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.
- [var backupFileURL: URL?](nsdocument/backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/scheduleautosaving())*