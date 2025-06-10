# unsafeLoad(fromByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Returns a new instance of the given type, constructed from the raw memory at the specified offset.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 12.2+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.1+
- watchOS 5.2+

## Declaration

```swift
func unsafeLoad<T>(fromByteOffset offset: Int = 0, as: T.Type) -> T
```

#### Return Value

A new instance of type `T`, read from the raw bytes at `offset`. The returned instance is memory-managed and unassociated with the value in the memory referenced by this pointer.

#### Discussion

The memory at this pointer plus `offset` must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.

This is an unsafe operation. Failure to meet the preconditions above may produce an invalid value of `T`.

## Parameters

- `offset`: The offset from this pointer, in bytes.   must be   nonnegative. The default is zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mutablerawspan/unsafeload(frombyteoffset:as:))*