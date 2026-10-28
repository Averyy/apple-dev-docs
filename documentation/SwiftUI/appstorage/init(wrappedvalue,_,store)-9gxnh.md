# init(wrappedValue:_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore a toolbarLabelStyle state.

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
init(wrappedValue: Value = ToolbarLabelStyle.automatic, _ key: String, store: UserDefaults? = nil) where Value == ToolbarLabelStyle
```

**Other overloads**:

```swift
init(wrappedValue: Value = TabViewCustomization(), _ key: String, store: UserDefaults? = nil) where Value == TabViewCustomization
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

## Parameters

- `wrappedValue`: The default value if toolbarLabelStyle state is not available for the given key.
- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)-9gxnh)*