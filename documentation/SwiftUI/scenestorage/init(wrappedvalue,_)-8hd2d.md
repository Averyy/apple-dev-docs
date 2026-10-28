# init(wrappedValue:_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore a string, transforming it to a `RawRepresentable` data type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == String
```

**Other overloads**:

```swift
init(wrappedValue: Value, _ key: String) where Value : RawRepresentable, Value.RawValue == Int
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

```swift
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
```

## Discussion

A common usage is with enumerations:

```swift
enum MyEnum: String {
    case a
    case b
    case c
}
struct MyView: View {
    @SceneStorage("MyEnumValue") private var value = MyEnum.a
    var body: some View { ... }
}
```

## Parameters

- `wrappedValue`: The default value if a String value is not available for the given key.
- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(wrappedvalue:_:)-8hd2d)*