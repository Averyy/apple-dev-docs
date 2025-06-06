# init(decoding:as:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a string from the given Unicode code units in the specified encoding.

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
init<C, Encoding>(decoding codeUnits: C, as sourceEncoding: Encoding.Type) where C : Collection, Encoding : _UnicodeEncoding, C.Element == Encoding.CodeUnit
```

## Parameters

- `codeUnits`: A collection of code units encoded in the encoding   specified in  .
- `sourceEncoding`: The encoding in which   should be   interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/init(decoding:as:))*