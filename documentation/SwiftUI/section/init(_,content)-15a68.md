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
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@export(implementation)
init(_ titleResource: LocalizedStringResource, @ContentBuilder content: () -> Content)
```

Available when `Parent` is `Text` and `Footer` is `EmptyView`.

**Other overloads**:

```swift
@export(implementation)
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: () -> Content)
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

- `titleResource`: The resource for the section’s localized title, which describes the contents of the section.
- `content`: The section’s content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/section/init(_:content:)-15a68)*