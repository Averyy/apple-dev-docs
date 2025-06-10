# decode(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Starts or continues decoding a code unit sequence into Unicode scalar values.

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
mutating func decode<I>(_ input: inout I) -> UnicodeDecodingResult where I : IteratorProtocol, Self.CodeUnit == I.Element
```

#### Return Value

A `UnicodeDecodingResult` instance, representing the next Unicode scalar, an indication of an error, or an indication that the UTF sequence has been fully decoded.

#### Discussion

To decode a code unit sequence completely, call this method repeatedly until it returns `UnicodeDecodingResult.emptyInput`. Checking that the iterator was exhausted is not sufficient, because the decoder can store buffered data from the input iterator.

Because of buffering, it is impossible to find the corresponding position in the iterator for a given returned `Unicode.Scalar` or an error.

The following example decodes the UTF-8 encoded bytes of a string into an array of `Unicode.Scalar` instances:

```swift
let str = "✨Unicode✨"
print(Array(str.utf8))
// Prints "[226, 156, 168, 85, 110, 105, 99, 111, 100, 101, 226, 156, 168]"

var bytesIterator = str.utf8.makeIterator()
var scalars: [Unicode.Scalar] = []
var utf8Decoder = UTF8()
Decode: while true {
    switch utf8Decoder.decode(&bytesIterator) {
    case .scalarValue(let v): scalars.append(v)
    case .emptyInput: break Decode
    case .error:
        print("Decoding error")
        break Decode
    }
}
print(scalars)
// Prints "["\u{2728}", "U", "n", "i", "c", "o", "d", "e", "\u{2728}"]"
```

## Parameters

- `input`: An iterator of code units to be decoded.   must be   the same iterator instance in repeated calls to this method. Do not   advance the iterator or any copies of the iterator outside this   method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicodecodec/decode(_:))*