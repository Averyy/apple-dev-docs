# decodeAtomicRepresentation(_:)

**Framework**: Swift  
**Kind**: method

Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.

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
static func decodeAtomicRepresentation(_ representation: consuming Optional<Wrapped>.AtomicRepresentation) -> Wrapped?
```

#### Return Value

The newly decoded logical type `Self`.

#### Discussion

> **Note**: This is not an atomic operation. This simply decodes the storage representation used in atomic operations back into the logical type for normal use, `Self`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/decodeatomicrepresentation(_:))*