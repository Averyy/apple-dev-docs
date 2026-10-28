# init(wrappedValue:_:store:)

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
init<RowValue>(wrappedValue: Value = TableColumnCustomization<RowValue>(), _ key: String, store: UserDefaults? = nil) where Value == TableColumnCustomization<RowValue>, RowValue : Identifiable
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

## Discussion

Table column state is typically not bound from a table directly to `AppStorage`, but instead indirecting through `State` or `SceneStorage`, and using the app storage value as its initial value kept up to date on changes to the direct backing.

## Parameters

- `wrappedValue`: The default value if table column state is not available for the given key.
- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)-5mu67)*