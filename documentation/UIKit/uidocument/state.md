# UIDocument.State

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the document state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
struct State
```

```c
enum UIDocumentState : NSUInteger;
```

## Overview

A [`UIDocument`](../uidocument.md) object stores the current state of the document in the [`documentState`](./documentstate.md) property. To receive notifications about changes in document state, observe the [`stateChangedNotification`](./statechangednotification.md) notification.

## Topics

### Constants
- [static var normal: UIDocument.State](./state/normal.md)
  The document is open, editing is enabled, and there are no conflicts or errors associated with it.
- [static var closed: UIDocument.State](./state/closed.md)
  There was an error in reading the document.
- [static var inConflict: UIDocument.State](./state/inconflict.md)
  Conflicts exist for the document file located at the file URL.
- [static var savingError: UIDocument.State](./state/savingerror.md)
  There was an error in saving or reverting the document.
- [static var editingDisabled: UIDocument.State](./state/editingdisabled.md)
  The document is busy and it isn’t currently safe for user edits.
- [static var progressAvailable: UIDocument.State](./state/progressavailable.md)
  The document is being downloaded or uploaded and progress information is available.
### Initializers
- [init(rawValue: UInt)](./state/init%28rawvalue%29.md)
  Creates a document state structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Constants
- [UIDocument.ChangeKind](./changekind.md)
  Constants that specify the kind of change to a document.
- [UIDocument.SaveOperation](./saveoperation.md)
  Constants that specify the type of save operation.
- [class let userActivityURLKey: String](./useractivityurlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/state)*