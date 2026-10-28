# init(wrappedValue:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore a Date.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
init(wrappedValue: Value, _ key: String) where Value == Date
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

```swift
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
```

## Parameters

- `wrappedValue`: The default value if a Date is not available for the given key.
- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:)-3a2up)*