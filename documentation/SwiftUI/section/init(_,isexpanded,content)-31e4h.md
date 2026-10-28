# init(_:isExpanded:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@export(implementation)
init<S>(_ title: S, isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content) where S : StringProtocol
```

Available when `Parent` is `Text` and `Footer` is `EmptyView`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, isExpanded: Binding<Bool>, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, isExpanded: Binding<Bool>, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

```swift
nonisolated
init<V, S>(_ title: S, isExpanded: Binding<Bool>, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, S : StringProtocol
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, isExpanded: Binding<Bool>, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

## Parameters

- `title`: A string that describes the contents of the section.
- `isExpanded`: A binding to a Boolean value that determines the section’s expansion state (expanded or collapsed).
- `content`: The section’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(_:isexpanded:content:)-31e4h)*