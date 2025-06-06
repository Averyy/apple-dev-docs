# loadUnaligned(fromByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.

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
func loadUnaligned<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T where T : BitwiseCopyable
```

#### Return Value

A new instance of type `T`, copied from the buffer pointer’s memory.

#### Discussion

This function only supports loading trivial types. A trivial type does not contain any reference-counted property within its in-memory stored representation. The memory at `offset` bytes into the buffer slice must be laid out identically to the in-memory representation of `T`.

You can use this method to create new values from the buffer pointer’s underlying bytes. The following example creates two new `Int32` instances from the memory referenced by the buffer pointer `someBytes`. The bytes for `a` are copied from the first four bytes of `someBytes`, and the bytes for `b` are copied from the fourth through seventh bytes.

```swift
let a = someBytes[..<4].loadUnaligned(as: Int32.self)
let b = someBytes[3...].loadUnaligned(as: Int32.self)
```

The memory to read for the new instance must not extend beyond the memory region represented by the buffer pointer slice—that is, `offset + MemoryLayout<T>.size` must be less than or equal to the slice’s `count`.

## Parameters

- `offset`: The offset into the slice’s memory, in bytes, at   which to begin reading data for the new instance. The default is zero.
- `type`: The type to use for the newly constructed instance. The memory   must be initialized to a value of a type that is layout compatible   with  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/slice/loadunaligned(frombyteoffset:as:)-6u1jm)*