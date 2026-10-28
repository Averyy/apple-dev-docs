# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unsortable column that generates its label from a string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: @escaping (RowValue) -> Content)
```

## Discussion

This initializer creates a [`Text`](../text.md) view for you, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). For information about localizing strings, see [`Text`](../text.md).

## Parameters

- `title`: A string that describes the column.
- `content`: The view content to display for each row in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:)-1lcze)*