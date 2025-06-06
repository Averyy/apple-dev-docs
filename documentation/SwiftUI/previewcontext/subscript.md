# subscript(_:)

**Framework**: SwiftUI  
**Kind**: subscript  
**Required**: Yes

Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key.

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
subscript<Key>(key: Key.Type) -> Key.Value where Key : PreviewContextKey { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/previewcontext/subscript(_:))*