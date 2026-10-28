# init(wrappedValue:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore table column state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
```

**Other overloads**:

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == Int
```

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == String
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Bool
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Data
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Date
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Double
```

```swift
init(wrappedValue: Value, _ key: String) where Value == Int
```

```swift
init(wrappedValue: Value, _ key: String) where Value == PersistentIdentifier
```

```swift
init(wrappedValue: Value, _ key: String) where Value == String
```

```swift
init(wrappedValue: Value, _ key: String) where Value == URL
```

## Parameters

- `wrappedValue`: The default value if table column state is not available for the given key.
- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:)-47bbm)*