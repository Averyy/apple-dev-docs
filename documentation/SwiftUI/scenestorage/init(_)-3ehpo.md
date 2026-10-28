# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore an Optional integer, transforming it to an Optional `RawRepresentable` data type.

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
init<R>(_ key: String) where Value == R?, R : RawRepresentable, R.RawValue == Int
```

**Other overloads**:

```swift
init(_ key: String) where Value == Bool?
```

```swift
init(_ key: String) where Value == Data?
```

```swift
init(_ key: String) where Value == Date?
```

```swift
init(_ key: String) where Value == Double?
```

```swift
init(_ key: String) where Value == Int?
```

```swift
init(_ key: String) where Value == PersistentIdentifier?
```

```swift
init(_ key: String) where Value == String?
```

```swift
init(_ key: String) where Value == URL?
```

```swift
init<R>(_ key: String) where Value == R?, R : RawRepresentable, R.RawValue == String
```

## Discussion

Defaults to nil if there is no restored value

A common usage is with enumerations:

```swift
enum MyEnum: Int {
    case a
    case b
    case c
}
struct MyView: View {
    @SceneStorage("MyEnumValue") private var value: MyEnum?
    var body: some View { ... }
}
```

## Parameters

- `key`: A key used to save and restore the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(_:)-3ehpo)*