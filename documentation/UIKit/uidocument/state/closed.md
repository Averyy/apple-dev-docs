# closed

**Framework**: UIKit  
**Kind**: property

There was an error in reading the document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static var closed: UIDocument.State { get }
```

#### Discussion

The document has either not been successfully opened, or has been since closed. The document properties might not be valid.

## See Also

- [static var normal: UIDocument.State](uidocument/state/normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var inConflict: UIDocument.State](uidocument/state/inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var savingError: UIDocument.State](uidocument/state/savingerror.md)
  There was an error in saving or reverting the document.
- [static var editingDisabled: UIDocument.State](uidocument/state/editingdisabled.md)
  The document is busy and it isn’t currently safe for user edits.
- [static var progressAvailable: UIDocument.State](uidocument/state/progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/closed)*