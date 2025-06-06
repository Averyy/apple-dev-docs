# init(unsafeUninitializedCapacity:initializingUTF8With:)

**Framework**: Swift  
**Kind**: init

Creates a new string with the specified capacity in UTF-8 code units, and then calls the given closure with a buffer covering the string’s uninitialized memory.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(unsafeUninitializedCapacity capacity: Int, initializingUTF8With initializer: (UnsafeMutableBufferPointer<UInt8>) throws -> Int) rethrows
```

#### Discussion

The closure should return the number of initialized code units, or 0 if it couldn’t initialize the buffer (for example if the requested capacity was too small).

This method replaces ill-formed UTF-8 sequences with the Unicode replacement character (`"\u{FFFD}"`). This may require resizing the buffer beyond its original capacity.

The following examples use this initializer with the contents of two different `UInt8` arrays—the first with a well-formed UTF-8 code unit sequence, and the second with an ill-formed sequence at the end.

```swift
let validUTF8: [UInt8] = [0x43, 0x61, 0x66, 0xC3, 0xA9]
let invalidUTF8: [UInt8] = [0x43, 0x61, 0x66, 0xC3]

let cafe1 = String(unsafeUninitializedCapacity: validUTF8.count) {
    _ = $0.initialize(from: validUTF8)
    return validUTF8.count
}
// cafe1 == "Café"

let cafe2 = String(unsafeUninitializedCapacity: invalidUTF8.count) {
    _ = $0.initialize(from: invalidUTF8)
    return invalidUTF8.count
}
// cafe2 == "Caf�"

let empty = String(unsafeUninitializedCapacity: 16) { _ in
    // Can't initialize the buffer (e.g. the capacity is too small).
    return 0
}
// empty == ""
```

## Parameters

- `capacity`: The number of UTF-8 code units worth of memory to allocate   for the string (excluding the null terminator).
- `initializer`: A closure that accepts a buffer covering uninitialized   memory with room for   UTF-8 code units, initializes   that memory, and returns the number of initialized elements.

## See Also

- [init(decoding: FilePath)](string/init(decoding:)-nm7v.md)
  Creates a string by interpreting the file path’s content as UTF-8 on Unix and UTF-16 on Windows.
- [init()](string/init.md)
  Creates an empty string.
- [init(Character)](string/init(_:)-8v3fo.md)
  Creates a string containing the given character.
- [init<S>(S)](string/init(_:)-8og6g.md)
  Creates a new string containing the characters in the given sequence.
- [init<S>(S)](string/init(_:)-1ip93.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](string/init(_:)-50pwi.md)
  Creates a new string containing the characters in the given sequence.
- [init(Substring)](string/init(_:)-14lv5.md)
  Creates a new string from the given substring.
- [init(repeating: String, count: Int)](string/init(repeating:count:)-23xjt.md)
  Creates a new string representing the given string repeated the specified number of times.
- [init(repeating: Character, count: Int)](string/init(repeating:count:)-11bpi.md)
  Creates a string representing the given character repeated the specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(unsafeuninitializedcapacity:initializingutf8with:))*