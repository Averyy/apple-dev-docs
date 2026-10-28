# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a property that can save and restore an Optional Date.

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
init(_ key: String) where Value == Date?
```

Available when `Value` conforms to `ExpressibleByNilLiteral`.

**Other overloads**:

```swift
init(_ key: String) where Value == Bool?
```

```swift
init(_ key: String) where Value == Data?
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scenestorage/init(_:)-3eghh)*