# load(fromByteOffset:as:)

**Framework**: Swift  
**Kind**: method

Returns a new instance of the given type, read from the buffer pointer’s raw memory at the specified byte offset.

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

A new instance of type `T`, copied from the buffer pointer’s memory.

#### Discussion

The memory at `offset` bytes from this buffer pointer’s `baseAddress` must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.

You can use this method to create new values from the buffer pointer’s underlying bytes. The following example creates two new `Int32` instances from the memory referenced by the buffer pointer `someBytes`. The bytes for `a` are copied from the first four bytes of `someBytes`, and the bytes for `b` are copied from the next four bytes.

```swift
let a = someBytes.load(as: Int32.self)
let b = someBytes.load(fromByteOffset: 4, as: Int32.self)
```

The memory to read for the new instance must not extend beyond the buffer pointer’s memory region—that is, `offset + MemoryLayout<T>.size` must be less than or equal to the buffer pointer’s `count`.

## Parameters

- `offset`: The offset, in bytes, into the buffer pointer’s memory at   which to begin reading data for the new instance. The buffer pointer   plus   must be properly aligned for accessing an instance of   type  . The default is zero.
- `type`: The type to use for the newly constructed instance. The memory   must be initialized to a value of a type that is layout compatible   with  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/load(frombyteoffset:as:))*