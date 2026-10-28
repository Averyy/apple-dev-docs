# init(_:store:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore an Optional string, transforming it to an Optional `RawRepresentable` data type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init<R>(_ key: String, store: UserDefaults? = nil) where Value == R?, R : RawRepresentable, R.RawValue == String
```

**Other overloads**:

```swift
init(_ key: String, store: UserDefaults? = nil) where Value == Bool?
```

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

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

```swift
enum MyEnum: String {
    case a
    case b
    case c
}
struct MyView: View {
    @AppStorage("MyEnumValue") private var value: MyEnum?
    var body: some View { ... }
}
```

## Parameters

- `key`: The key to read and write the value to in the user defaults store.
- `store`: The user defaults store to read and write to. A value of `nil` will use the user default store from the environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/appstorage/init(_:store:)-6aj8x)*