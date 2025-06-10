# progressAvailable

**Framework**: UIKit  
**Kind**: property

The document is being downloaded or uploaded and progress information is available.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static var progressAvailable: UIDocument.State { get }
```

#### Discussion

When this state is set, you can use the [`progress`](https://developer.apple.com/documentation/Foundation/ProgressReporting/progress) property of the document to monitor the current operation.

## See Also

- [static var normal: UIDocument.State](uidocument/state/normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](uidocument/state/closed.md)
  There was an error in reading the document.
- [static var inConflict: UIDocument.State](uidocument/state/inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var savingError: UIDocument.State](uidocument/state/savingerror.md)
  There was an error in saving or reverting the document.
- [static var editingDisabled: UIDocument.State](uidocument/state/editingdisabled.md)
  The document is busy and it isn’t currently safe for user edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state/progressavailable)*