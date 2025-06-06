# init(bitPattern:)

**Framework**: Swift  
**Kind**: init

Creates a new value with the bit pattern of the given pointer.

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
init<P>(bitPattern pointer: P?) where P : _Pointer
```

#### Discussion

The new value represents the address of the pointer passed as `pointer`. If `pointer` is `nil`, the result is `0`.

## Parameters

- `pointer`: The pointer to use as the source for the new   integer.

## See Also

- [init(bitPattern: ObjectIdentifier)](int/init(bitpattern:)-2o9co.md)
  Creates an integer that captures the full value of the given object identifier.
- [init(bitPattern: OpaquePointer?)](int/init(bitpattern:)-5qm7a.md)
  Creates a new value with the bit pattern of the given pointer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(bitpattern:)-2i0qy)*