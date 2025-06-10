# subscript(_:)

**Framework**: Swift  
**Kind**: subscript

Accesses the element at the specified position.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
subscript(position: KeyValuePairs<Key, Value>.Index) -> KeyValuePairs<Key, Value>.Element { get }
```

#### Return Value

The key-value pair at position `position`.

## Parameters

- `position`: The position of the element to access.    must be a valid index of the collection that is not equal to the    property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/keyvaluepairs/subscript(_:))*