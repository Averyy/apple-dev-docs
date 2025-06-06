# load(fromByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

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
func load<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T
```

#### Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance is memory-managed and unassociated with the value in the memory referenced by this pointer.

#### Discussion

The memory at this pointer plus `offset` must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.

## Parameters

- `offset`: The offset from this pointer, in bytes.   must be   nonnegative. The default is zero.
- `type`: The type of the instance to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsaferawpointer/load(frombyteoffset:as:))*