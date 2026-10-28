# init(validatingUTF8:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 6.0 (renamed: String.init(validatingCString:))

## Declaration

```swift
init?(validatingUTF8 cString: UnsafePointer<CChar>)
```

## Discussion

This initializer does not try to repair ill-formed UTF-8 code unit sequences. If any are found, the result of the initializer is `nil`.

The following example calls this initializer with pointers to the contents of two different `CChar` arrays—the first with well-formed UTF-8 code unit sequences and the second with an ill-formed sequence at the end.

```swift
let validUTF8: [CChar] = [67, 97, 102, -61, -87, 0]
validUTF8.withUnsafeBufferPointer { ptr in
    let s = String(validatingUTF8: ptr.baseAddress!)
    print(s)
}
// Prints "Optional("Café")"

let invalidUTF8: [CChar] = [67, 97, 102, -61, 0]
invalidUTF8.withUnsafeBufferPointer { ptr in
    let s = String(validatingUTF8: ptr.baseAddress!)
    print(s)
}
// Prints "nil"
```

> **Note**: This initializer has been renamed. Use `String.init?(validatingCString:)` instead.

## Parameters

- `cString`:  A pointer to a null-terminated sequence of UTF-8 code units.

## See Also

### Creating a String from Unicode Data
- [init(Unicode.Scalar)](./init%28_%29-8ay23.md)
- [init?(data: Data, encoding: String.Encoding)](./init%28data,encoding%29.md)
  Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init?<Encoding>(validating: some Sequence, as: Encoding.Type)](./init%28validating,as%29-84qr9.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?<Encoding>(validating: some Sequence<Int8>, as: Encoding.Type)](./init%28validating,as%29-5cw2c.md)
  Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init?(utf8String: [CChar])](./init%28utf8string%29-8qmaq.md)
  Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init?(utf8String: UnsafePointer<CChar>)](./init%28utf8string%29-3mcco.md)
  Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits: UnsafePointer<unichar>, count: Int)](./init%28utf16codeunits,count%29.md)
  Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count: Int, freeWhenDone: Bool)](./init%28utf16codeunitsnocopy,count,freewhendone%29.md)
  Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units.
- [init<C, Encoding>(decoding: C, as: Encoding.Type)](./init%28decoding,as%29.md)
  Creates a string from the given Unicode code units in the specified encoding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(validatingutf8:)-208fn)*