# UIDocument.ChangeKind

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the kind of change to a document.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
enum ChangeKind
```

```c
enum UIDocumentChangeKind : NSInteger;
```

#### Overview

You specify one of these constants as a parameter of the [`updateChangeCount(_:)`](./updatechangecount%28_%29.md) method.

## Topics

### Constants
- [UIDocument.ChangeKind.done](./changekind/done.md)
  A change has been made to the document.
- [UIDocument.ChangeKind.undone](./changekind/undone.md)
  A change to the document has been undone.
- [UIDocument.ChangeKind.redone](./changekind/redone.md)
  An undone change to the document has been redone.
- [UIDocument.ChangeKind.cleared](./changekind/cleared.md)
  The document is cleared of outstanding changes.
### Initializers
- [init?(rawValue: Int)](./changekind/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [UIDocument.SaveOperation](./saveoperation.md)
  Constants that specify the type of save operation.
- [UIDocument.State](./state.md)
  Constants that specify the document state.
- [class let userActivityURLKey: String](./useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/changekind)*