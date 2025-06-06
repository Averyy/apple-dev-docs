# decodeAtomicRepresentation(_:)

**Framework**: Synchronization  
**Kind**: method  
**Required**: Yes

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
static func decodeAtomicRepresentation(_ storage: consuming Self.AtomicRepresentation) -> Self
```

#### Return Value

The newly decoded logical type `Self`.

#### Discussion

> **Note**: This is not an atomic operation. This simply decodes the storage representation used in atomic operations back into the logical type for normal use, `Self`.

This is not an atomic operation. This simply decodes the storage representation used in atomic operations back into the logical type for normal use, `Self`.

## Parameters

- `storage`: The storage representation for   that’s used   within atomic operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicrepresentable/decodeatomicrepresentation(_:))*