# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a disclosure group, using a provided string to create a text view for the label.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ label: S, @ContentBuilder content: @escaping () -> Content) where S : StringProtocol
```

Available when `Label` is `Text` and `Content` conforms to `View`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: @escaping () -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: @escaping () -> Content)
```

## Parameters

- `label`: A description of the content of the disclosure group.
- `content`: The content shown when the disclosure group expands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/disclosuregroup/init(_:content:)-9byxn)*