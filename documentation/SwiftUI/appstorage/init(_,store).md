# init(_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can read and write an Optional boolean user default.

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
init(_ key: String, store: UserDefaults? = nil) where Value == Bool?
```

Available when `Value` conforms to `ExpressibleByNilLiteral`.

**Other overloads**:

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Data?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Date?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Double?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Int?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == PersistentIdentifier?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == String?
```

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == URL?
```

```swift
init<R>(_ key: String, store: UserDefaults? = nil) where Value == R?, R : RawRepresentable, R.RawValue == Int
```

```swift
init<R>(_ key: String, store: UserDefaults? = nil) where Value == R?, R : RawRepresentable, R.RawValue == String
```

## Discussion

Defaults to nil if there is no restored value.

## Parameters

- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.

## See Also

### Storing a value
- [init(wrappedValue:_:store:)](./init%28wrappedvalue,_,store%29.md)
  Creates a property that can save and restore tab sidebar customizations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(_:store:))*