# init(wrappedValue:_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore tab sidebar customizations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
```

**Other overloads**:

```swift
init(wrappedValue: Value = ToolbarLabelStyle.automatic, _ key: String, store: UserDefaults? = nil) where Value == ToolbarLabelStyle
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value : RawRepresentable, Value.RawValue == Int
```

```swift
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value : RawRepresentable, Value.RawValue == String
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

You can set this customization on the TabView using [`tabViewCustomization(_:)`](../view/tabviewcustomization%28_%29.md).

## Parameters

- `wrappedValue`: The default value if the customization is not available for the given key.
- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.

## See Also

### Storing a value
- [init(_:store:)](./init%28_,store%29.md)
  Creates a property that can read and write an Optional boolean user default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:))*