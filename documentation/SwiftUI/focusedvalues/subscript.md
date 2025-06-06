# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript

Reads and writes values associated with a given focused value key.

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
subscript<Key>(key: Key.Type) -> Key.Value? where Key : FocusedValueKey { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalues/subscript(_:))*