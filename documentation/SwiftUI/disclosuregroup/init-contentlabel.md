# init(content:label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a disclosure group with the given label and content views.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(@ViewBuilder content: @escaping () -> Content, @ViewBuilder label: () -> Label)
```

## Parameters

- `content`: The content shown when the disclosure group expands.
- `label`: A view that describes the content of the disclosure group.

## See Also

- [init(_:content:)](disclosuregroup/init(_:content:).md)
  Creates a disclosure group, using a provided localized string key to create a text view for the label.
- [init(_:isExpanded:content:)](disclosuregroup/init(_:isexpanded:content:).md)
  Creates a disclosure group, using a provided localized string key to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)](disclosuregroup/init(isexpanded:content:label:).md)
  Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(content:label:))*