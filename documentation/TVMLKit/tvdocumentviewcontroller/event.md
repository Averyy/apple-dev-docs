# TVDocumentViewController.Event

**Framework**: TVMLKit  
**Kind**: struct

Events that can be triggered on the document view controller.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
struct Event
```

## Topics

### Initializers for Document View Controller Events
- [init(String)](tvdocumentviewcontroller/event/init(_:).md)
  Create a new document view controller event based on a string value.
- [init(rawValue: String)](tvdocumentviewcontroller/event/init(rawvalue:).md)
  Create an instance of a new document view controller event based on a string value.
### Event Types
- [static let appear: TVDocumentViewController.Event](tvdocumentviewcontroller/event/appear.md)
  An event that signals when the document appears.
- [static let disappear: TVDocumentViewController.Event](tvdocumentviewcontroller/event/disappear.md)
  An event that signals when the document disappears.
- [static let highlight: TVDocumentViewController.Event](tvdocumentviewcontroller/event/highlight.md)
  An event that signals when the document is highlighted.
- [static let holdSelect: TVDocumentViewController.Event](tvdocumentviewcontroller/event/holdselect.md)
  An event that signals when the document is held down and selected.
- [static let load: TVDocumentViewController.Event](tvdocumentviewcontroller/event/load.md)
  An event that signals when the document is loaded.
- [static let play: TVDocumentViewController.Event](tvdocumentviewcontroller/event/play.md)
  An event that signals when the document is played.
- [static let select: TVDocumentViewController.Event](tvdocumentviewcontroller/event/select.md)
  An event that signals when the document is selected.
- [static let unload: TVDocumentViewController.Event](tvdocumentviewcontroller/event/unload.md)
  An event that signals when the document is unloaded.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvdocumentviewcontroller/event)*