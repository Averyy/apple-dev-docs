# init(_:value:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column for 64-bit integer values that displays a string property.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int64>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

Available when `RowValue` inherits `NSObject`, `RowValue` conforms to `Identifiable`, `Sort` is `SortDescriptor<RowValue>`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Bool>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Bool?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Date>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Date?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Double>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Double?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Float>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Float?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, Int?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UInt?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UUID>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, UUID?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
@export(implementation)
nonisolated init<V>(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, V>, @ContentBuilder content: @escaping (RowValue) -> Content) where V : Comparable
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Bool>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Bool?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Date>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Date?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Double>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Double?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Float>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Float?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, Int?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UInt?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UUID>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, UUID?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Bool>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Bool?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Date>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Date?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Double>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Double?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Float>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Float?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, Int?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt16>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt16?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt32>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt32?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt64>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt64?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt8>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt8?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UInt?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UUID>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, UUID?>, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init<S, V>(_ title: S, value: KeyPath<RowValue, V>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol, V : Comparable
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Bool>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Bool?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Date>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Date?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Double>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Double?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Float>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Float?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int16>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int16?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int32>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int32?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int64?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int8>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int8?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, Int?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt16>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt16?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt32>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt32?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt64>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt64?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt8>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt8?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UInt?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UUID>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, UUID?>, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

```swift
nonisolated
init<V>(_ text: Text, value: KeyPath<RowValue, V>, @ContentBuilder content: @escaping (RowValue) -> Content) where V : Comparable
```

```swift
nonisolated
init<V>(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, V>, @ContentBuilder content: @escaping (RowValue) -> Content) where V : Comparable
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). For more information about localizing strings, see [`Text`](../text.md).

## Parameters

- `title`: A string that describes the column.
- `value`: The path to the property associated with the column, used to update the table’s sorting state.
- `content`: The view content to display for each row in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:content:)-nlm)*