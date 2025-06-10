# decode(_:)

**Framework**: Swift  
**Kind**: method

Starts or continues decoding a UTF-32 sequence.

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
mutating func decode<I>(_ input: inout I) -> UnicodeDecodingResult where I : IteratorProtocol, I.Element == UInt32
```

#### Return Value

A `UnicodeDecodingResult` instance, representing the next Unicode scalar, an indication of an error, or an indication that the UTF sequence has been fully decoded.

#### Discussion

To decode a code unit sequence completely, call this method repeatedly until it returns `UnicodeDecodingResult.emptyInput`. Checking that the iterator was exhausted is not sufficient, because the decoder can store buffered data from the input iterator.

Because of buffering, it is impossible to find the corresponding position in the iterator for a given returned `Unicode.Scalar` or an error.

The following example decodes the UTF-16 encoded bytes of a string into an array of `Unicode.Scalar` instances. This is a demonstration only—if you need the Unicode scalar representation of a string, use its `unicodeScalars` view.

```swift
// UTF-32 representation of "✨Unicode✨"
let codeUnits: [UTF32.CodeUnit] =
        [10024, 85, 110, 105, 99, 111, 100, 101, 10024]

var codeUnitIterator = codeUnits.makeIterator()
var scalars: [Unicode.Scalar] = []
var utf32Decoder = UTF32()
Decode: while true {
    switch utf32Decoder.decode(&codeUnitIterator) {
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/utf32/decode(_:)-swift.method)*