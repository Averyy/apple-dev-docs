# encodeAtomicOptionalRepresentation(_:)

**Framework**: Swift  
**Kind**: method

Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.

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
static func encodeAtomicOptionalRepresentation(_ value: consuming Self?) -> Self.RawValue.AtomicOptionalRepresentation
```

#### Return Value

The newly encoded `AtomicOptionalRepresentation` storage.

#### Discussion

> **Note**: This is not an atomic operation. This simply encodes the logical type `Self` into its storage representation suitable for atomic operations, `AtomicOptionalRepresentation`.

This is not an atomic operation. This simply encodes the logical type `Self` into its storage representation suitable for atomic operations, `AtomicOptionalRepresentation`.

## Parameters

- `value`: An optional instance of   that’s about to be   destroyed to encode an instance of its  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable/encodeatomicoptionalrepresentation(_:))*