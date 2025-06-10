# encode(_:into:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes a Unicode scalar as a series of code units by calling the given closure on each code unit.

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
static func encode(_ input: Unicode.Scalar, into processCodeUnit: (Self.CodeUnit) -> Void)
```

#### Discussion

For example, the musical fermata symbol (“𝄐”) is a single Unicode scalar value (`\u{1D110}`) but requires four code units for its UTF-8 representation. The following code uses the `UTF8` codec to encode a fermata in UTF-8:

```swift
var bytes: [UTF8.CodeUnit] = []
UTF8.encode("𝄐", into: { bytes.append($0) })
print(bytes)
// Prints "[240, 157, 132, 144]"
```

## Parameters

- `input`: The Unicode scalar value to encode.
- `processCodeUnit`: A closure that processes one code unit argument at a   time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicodecodec/encode(_:into:))*