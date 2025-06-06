# autosave(withDelegate:didAutosave:contextInfo:)

**Framework**: AppKit  
**Kind**: method

Autosaves the document’s contents to an appropriate location in the file system.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func autosave(withDelegate delegate: Any?, didAutosave didAutosaveSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

After autosaving, sends the message selected by `didAutosaveSelector` to the delegate, with `contextInfo` as the last argument. The method selected by `didAutosaveSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didAutosave:(BOOL)didAutosaveSuccessfully contextInfo:(void *)contextInfo
```

If an error occurs while autosaving, the method reports it to the user before sending the delegate a `succeeded:NO` message.

## Parameters

- `delegate`: The delegate to which the selector message is sent.
- `didAutosaveSelector`: The selector of the message sent to the delegate.
- `contextInfo`: Object passed with the callback to provide any additional context information.

## See Also

- [var autosavedContentsFileURL: URL?](nsdocument/autosavedcontentsfileurl.md)
  The location of the most recently autosaved document contents.
- [func checkAutosavingSafety() throws](nsdocument/checkautosavingsafety.md)
  Returns a Boolean value that indicates whether it is safe to autosave document changes.
- [var hasUnautosavedChanges: Bool](nsdocument/hasunautosavedchanges.md)
  A Boolean value that indicates whether the document has changes that have not been autosaved.
- [func scheduleAutosaving()](nsdocument/scheduleautosaving.md)
  Schedules periodic autosaving for the purpose of crash protection.
- [func autosave(withImplicitCancellability: Bool, completionHandler: ((any Error)?) -> Void)](nsdocument/autosave(withimplicitcancellability:completionhandler:).md)
  Autosaves the document’s contents to an appropriate file-system location, as needed.
- [var backupFileURL: URL?](nsdocument/backupfileurl.md)
  The URL for the document’s backup file that was created during an autosave operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/autosave(withdelegate:didautosave:contextinfo:))*