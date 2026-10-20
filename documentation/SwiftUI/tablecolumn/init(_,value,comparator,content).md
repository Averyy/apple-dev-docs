# init(_:value:comparator:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column that generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to `Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String?>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init<V, C>(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, V>, comparator: C, @ContentBuilder content: @escaping (RowValue) -> Content) where V == C.Compared, C : SortComparator
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String?>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, String?>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init<S, V, C>(_ title: S, value: KeyPath<RowValue, V>, comparator: C, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol, V == C.Compared, C : SortComparator
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, String?>, comparator: String.StandardComparator = .localizedStandard, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<V, C>(_ text: Text, value: KeyPath<RowValue, V>, comparator: C, @ContentBuilder content: @escaping (RowValue) -> Content) where V == C.Compared, C : SortComparator
```

```swift
nonisolated
init<V, C>(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, V>, comparator: C, @ContentBuilder content: @escaping (RowValue) -> Content) where V == C.Compared, C : SortComparator
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. See [`Text`](../text.md) for more information about localizing strings.

## Parameters

- `value`: The path to the property associated with the column, used to update the table’s sorting state.
- `comparator`: The specific comparator to compare string values.
- `content`: The view content to display for each row in a table.

## See Also

### Creating a sortable column
- [init(_:value:content:)](./init%28_,value,content%29.md)
  Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:)](./init%28_,value,comparator%29.md)
  Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:sortUsing:content:)](./init%28_,sortusing,content%29.md)
  Creates a sortable column that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:content:))*