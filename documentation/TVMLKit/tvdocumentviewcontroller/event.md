# TVDocumentViewController.Event

**Framework**: TVMLKit  
**Kind**: struct  
**Role**: Structure

Events that can be triggered on the document view controller.

**Availability**:
- tvOS 13.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
struct Event
```

```c
typedef NSString * TVDocumentEvent;
```

## Topics

### Initializers for Document View Controller Events
- [init(String)](./event/init%28_%29.md)
  Create a new document view controller event based on a string value.
- [init(rawValue: String)](./event/init%28rawvalue%29.md)
  Create an instance of a new document view controller event based on a string value.
### Event Types
- [static let appear: TVDocumentViewController.Event](./event/appear.md)
  An event that signals when the document appears.
- [static let disappear: TVDocumentViewController.Event](./event/disappear.md)
  An event that signals when the document disappears.
- [static let highlight: TVDocumentViewController.Event](./event/highlight.md)
  An event that signals when the document is highlighted.
- [static let holdSelect: TVDocumentViewController.Event](./event/holdselect.md)
  An event that signals when the document is held down and selected.
- [static let load: TVDocumentViewController.Event](./event/load.md)
  An event that signals when the document is loaded.
- [static let play: TVDocumentViewController.Event](./event/play.md)
  An event that signals when the document is played.
- [static let select: TVDocumentViewController.Event](./event/select.md)
  An event that signals when the document is selected.
- [static let unload: TVDocumentViewController.Event](./event/unload.md)
  An event that signals when the document is unloaded.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/event)*