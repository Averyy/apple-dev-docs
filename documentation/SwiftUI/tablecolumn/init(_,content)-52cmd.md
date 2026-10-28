# init(_:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unsortable column that generates its label from a localized string key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, @ContentBuilder content: @escaping (RowValue) -> Content)
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
init<S>(_ title: S, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view for you, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). For more information about localizing strings, see [`Text`](../text.md).

## Parameters

- `titleKey`: The key for the column’s localized title.
- `content`: The view content to display for each row in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:content:)-52cmd)*