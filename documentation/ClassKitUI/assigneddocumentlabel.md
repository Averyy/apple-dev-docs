# AssignedDocumentLabel

**Framework**: ClassKit UI  
**Kind**: struct

A view that displays the status or date information of the assigned document.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency struct AssignedDocumentLabel
```

#### Overview

`AssignedDocumentLabel` displays information about an assigned document for students, including submission status and relevant dates like due dates. The view automatically updates its appearance based on assigned document state, showing past-due items in red.

```swift
VStack(alignment: .leading) {
    Text("My Document")
        .font(.headline)

    HStack {
        AssignedDocumentLabel(role: .status, documentURL: documentURL)
        AssignedDocumentLabel(role: .date, documentURL: documentURL)
    }
    .font(.caption)
}
```

## Topics

### Structures
- [AssignedDocumentLabel.Role](assigneddocumentlabel/role.md)
  The type of assignment information to display.
### Initializers
- [init(role: AssignedDocumentLabel.Role, documentURL: URL)](assigneddocumentlabel/init(role:documenturl:).md)
  Creates a label that displays information about the assigned document.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitui/assigneddocumentlabel)*