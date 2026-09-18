# subscript(_:)

**Framework**: Foundation Models  
**Kind**: subscript

Accesses the value stored for the given session property key.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
final subscript<K>(key: K.Type) -> K.Value where K : SessionPropertyKey { get set }
```

## Parameters

- `key`: The session property key type whose value to read or write.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/sessionpropertyvalues/subscript(_:))*