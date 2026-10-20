# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Role**: Instance Subscript  
**Required**: Yes

Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0
- iPadOS 14.0+ - Deprecated in 27.0
- Mac Catalyst 14.0+ - Deprecated in 27.0
- macOS 11.0+ - Deprecated in 27.0
- tvOS 14.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 7.0+ - Deprecated in 27.0

> **Deprecated**: Use #Preview with a Widget timeline provider or entries instead.

## Declaration

```swift
subscript<Key>(key: Key.Type) -> Key.Value where Key : PreviewContextKey { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontext/subscript(_:))*