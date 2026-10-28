# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore an Optional boolean.

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
init(_ key: String) where Value == Bool?
```

Available when `Value` conforms to `ExpressibleByNilLiteral`.

**Other overloads**:

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
init<R>(_ key: String) where Value == R?, R : RawRepresentable, R.RawValue == Int
```

```swift
init<R>(_ key: String) where Value == R?, R : RawRepresentable, R.RawValue == String
```

## Discussion

Defaults to nil if there is no restored value

## Parameters

- `key`: A key used to save and restore the value.

## See Also

### Storing a value
- [init(wrappedValue:_:)](./init%28wrappedvalue,_%29.md)
  Creates a property that can save and restore an integer, transforming it to a `RawRepresentable` data type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(_:))*