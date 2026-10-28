# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<V, S>(_ title: S, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, S : StringProtocol
```

Available when `Parent` conforms to `TableRowContent`, `Content` conforms to `TableRowContent`, and `Footer` conforms to `TableRowContent`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

```swift
@export(implementation)
init<S>(_ title: S, @ContentBuilder content: () -> Content) where S : StringProtocol
```

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

## Parameters

- `title`: A string that describes the contents of the section.
- `content`: The section’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(_:content:)-5ax3j)*