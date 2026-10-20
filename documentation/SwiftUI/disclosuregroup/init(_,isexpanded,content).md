# init(_:isExpanded:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

```swift
nonisolated
init<S>(_ label: S, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content) where S : StringProtocol
```

## Parameters

- `titleResource`: The localized label of `self` that describes the content of the disclosure group.
- `isExpanded`: A binding to a Boolean value that determines the group’s expansion state (expanded or collapsed).
- `content`: The content shown when the disclosure group expands.

## See Also

### Creating a disclosure group
- [init(_:content:)](./init%28_,content%29.md)
  Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(content: () -> Content, label: () -> Label)](./init%28content,label%29.md)
  Creates a disclosure group with the given label and content views.
- [init(isExpanded: Binding<Bool>, content: () -> Content, label: () -> Label)](./init%28isexpanded,content,label%29.md)
  Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(_:isexpanded:content:))*