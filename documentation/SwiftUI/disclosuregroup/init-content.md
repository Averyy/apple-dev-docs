# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init

Creates a disclosure group, using a provided localized string resource to create a text view for the label.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `titleResource`: The localized label of `self` that describes the content of the disclosure group.
- `content`: The content shown when the disclosure group expands.

## See Also

- [init(content: () -> Content, label: () -> Label)](disclosuregroup/init(content:label:).md)
  Creates a disclosure group with the given label and content views.
- [init(_:isExpanded:content:)](disclosuregroup/init(_:isexpanded:content:).md)
  Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)](disclosuregroup/init(isexpanded:content:label:).md)
  Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(_:content:))*