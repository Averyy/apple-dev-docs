# encodeAtomicRepresentation(_:)

**Framework**: Swift  
**Kind**: method

Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.

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
static func encodeAtomicRepresentation(_ value: borrowing Int16) -> Int16.AtomicRepresentation
```

#### Return Value

The newly encoded `AtomicRepresentation` storage.

#### Discussion

> **Note**: This is not an atomic operation. This simply encodes the logical type `Self` into its storage representation suitable for atomic operations, `AtomicRepresentation`.

## Parameters

- `value`: A valid instance of   that’s about to be destroyed   to encode an instance of its  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/encodeatomicrepresentation(_:))*