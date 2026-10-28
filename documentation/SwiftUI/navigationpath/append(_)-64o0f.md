# append(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Appends a new value to the end of this path.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func append<V>(_ value: V) where V : Hashable
```

**Other overloads**:

```swift
mutating func append<V>(_ value: V) where V : Decodable, V : Encodable, V : Hashable
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/navigationpath/append(_:)-64o0f)*