# UIDocument.State

**Framework**: UIKit  
**Kind**: struct

Constants that specify the document state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
struct State
```

#### Overview

A [`UIDocument`](uidocument.md) object stores the current state of the document in the [`documentState`](uidocument/documentstate.md) property. To receive notifications about changes in document state, observe the [`stateChangedNotification`](uidocument/statechangednotification.md) notification.

## Topics

### Constants
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
- [static var progressAvailable: UIDocument.State](uidocument/state/progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.
### Initializers
- [init(rawValue: UInt)](uidocument/state/init(rawvalue:).md)
  Creates a document state structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [UIDocument.ChangeKind](uidocument/changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.SaveOperation](uidocument/saveoperation.md)
  Constants that specify the type of save operation.
- [class let userActivityURLKey: String](uidocument/useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state)*