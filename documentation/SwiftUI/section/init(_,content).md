# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a section with the provided section content.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@export(implementation)
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
```

Available when `Parent` is `Text` and `Footer` is `EmptyView`.

**Other overloads**:

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
init<V, S>(_ title: S, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue, S : StringProtocol
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, @TableRowBuilder<V> content: () -> Content) where Parent == TableHeaderRowContent<V, Text>, Footer == EmptyTableRowContent<V>, V == Content.TableRowValue
```

## Parameters

- `titleKey`: The key for the section’s localized title, which describes the contents of the section.
- `content`: The section’s content.

## See Also

### Creating a section
- [init(content:)](./init%28content%29.md)
  Creates a section with the provided section content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(_:content:))*