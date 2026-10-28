# init(wrappedValue:_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can read and write to a user default as data.

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
init(wrappedValue: Value, _ key: String, store: UserDefaults? = nil) where Value == Data
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

Avoid storing large data blobs in user defaults, such as image data, as it can negatively affect performance of your app. On tvOS, a `NSUserDefaultsSizeLimitExceededNotification` notification is posted if the total user default size reaches 512kB.

## Parameters

- `wrappedValue`: The default value if a data value is not specified for the given key.
- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(wrappedvalue:_:store:)-33hrf)*