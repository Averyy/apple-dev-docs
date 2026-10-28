# init(wrappedValue:_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can read and write to a string user default, transforming that to `RawRepresentable` data type.

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
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value : RawRepresentable, Value.RawValue == String
```

**Other overloads**:

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
```

```swift
init(wrappedValue: Value = ToolbarLabelStyle.automatic, _ key: String, store: UserDefaults? = nil) where Value == ToolbarLabelStyle
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value : RawRepresentable, Value.RawValue == Int
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Bool
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Data
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Date
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Double
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Int
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == PersistentIdentifier
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == String
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == URL
```

```swift
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String, store: UserDefaults? = nil) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
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
    @AppStorage("MyEnumValue") private var value = MyEnum.a
    var body: some View { ... }
}
```

## Parameters

- `wrappedValue`: The default value if a string value is not specified for the given key.
- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)-7zk4r)*