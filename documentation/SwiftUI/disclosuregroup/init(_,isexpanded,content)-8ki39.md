# init(_:isExpanded:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a disclosure group, using a provided localized string key to create a text view for the label, and a binding to the expansion state (expanded or collapsed).

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content)
```

```swift
nonisolated
init<S>(_ label: S, isExpanded: Binding<Bool>, @ContentBuilder content: @escaping () -> Content) where S : StringProtocol
```

## Parameters

- `titleKey`: The key for the localized label of `self` that describes the content of the disclosure group.
- `isExpanded`: A binding to a Boolean value that determines the group’s expansion state (expanded or collapsed).
- `content`: The content shown when the disclosure group expands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(_:isexpanded:content:)-8ki39)*