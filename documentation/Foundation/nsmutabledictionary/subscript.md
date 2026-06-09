# subscript(_:)

**Framework**: Foundation  
**Kind**: subscript

Accesses the value associated with a given key.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@objc
override dynamic subscript(key: Any) -> Any? { get set }
```

#### Return Value

The value associated with the key, or `nil` if no value is associated with the key.

## Parameters

- `key`: The key whose value you want to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutabledictionary/subscript(_:))*