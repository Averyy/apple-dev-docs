# decodeAtomicOptionalRepresentation(_:)

**Framework**: Swift  
**Kind**: method

Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.

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
static func decodeAtomicOptionalRepresentation(_ representation: consuming ObjectIdentifier.AtomicOptionalRepresentation) -> ObjectIdentifier?
```

#### Return Value

The newly decoded logical type `Self?`.

#### Discussion

> **Note**: This is not an atomic operation. This simply decodes the storage representation used in atomic operations on `Optional` back into the logical type for normal use, `Self?`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/objectidentifier/decodeatomicoptionalrepresentation(_:))*