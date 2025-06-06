# UIDocument.ChangeKind

**Framework**: UIKit  
**Kind**: enum

Constants that specify the kind of change to a document.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
enum ChangeKind
```

#### Overview

You specify one of these constants as a parameter of the [`updateChangeCount(_:)`](uidocument/updatechangecount(_:).md) method.

## Topics

### Constants
- [UIDocument.ChangeKind.done](uidocument/changekind/done.md)
  A change has been made to the document.
- [UIDocument.ChangeKind.undone](uidocument/changekind/undone.md)
  A change to the document has been undone.
- [UIDocument.ChangeKind.redone](uidocument/changekind/redone.md)
  An undone change to the document has been redone.
- [UIDocument.ChangeKind.cleared](uidocument/changekind/cleared.md)
  The document is cleared of outstanding changes.
### Initializers
- [init?(rawValue: Int)](uidocument/changekind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [UIDocument.SaveOperation](uidocument/saveoperation.md)
  Constants that specify the type of save operation.
- [UIDocument.State](uidocument/state.md)
  Constants that specify the document state.
- [class let userActivityURLKey: String](uidocument/useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/changekind)*