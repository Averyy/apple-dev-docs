# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a disclosure group with the given label and content views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(@ContentBuilder content: @escaping () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content`: The content shown when the disclosure group expands.
- `label`: A view that describes the content of the disclosure group.

## See Also

### Creating a disclosure group
- [init(_:content:)](./init%28_,content%29.md)
  Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(_:isExpanded:content:)](./init%28_,isexpanded,content%29.md)
  Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)](./init%28isexpanded,content,label%29.md)
  Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(content:label:))*