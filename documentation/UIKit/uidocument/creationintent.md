# UIDocument.CreationIntent

**Framework**: UIKit  
**Kind**: struct

An app intent that creates new documents for your app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- visionOS 2.0+

## Declaration

```swift
struct CreationIntent
```

## Mentions

- [Customizing a document-based app’s launch experience](customizing-a-document-based-app-s-launch-experience.md)

#### Overview

UIKit provides a default intent. You can extend this structure to provide additional intents for your app.

```swift
// Extend the creation intent enumeration to add custom options for document creation.
extension UIDocument.CreationIntent {
    static let template = UIDocument.CreationIntent("template")
}
```

For more information, see [`Customizing a document-based app’s launch experience`](customizing-a-document-based-app-s-launch-experience.md).

## Topics

### Accessing creation intents
- [static let `default`: UIDocument.CreationIntent](uidocument/creationintent/default.md)
  The default document creation intent.
### Creating new intents
- [init(String)](uidocument/creationintent/init(_:).md)
  Create a new document creation intent using the provided string.
- [init(rawValue: String)](uidocument/creationintent/init(rawvalue:).md)
  Create a new document creation intent using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/creationintent)*