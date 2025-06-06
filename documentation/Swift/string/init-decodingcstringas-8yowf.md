# init(decodingCString:as:)

**Framework**: Swift  
**Kind**: init

Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.

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
init<Encoding>(decodingCString nullTerminatedCodeUnits: UnsafePointer<Encoding.CodeUnit>, as encoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

#### Discussion

If `nullTerminatedCodeUnits` contains ill-formed code unit sequences, this initializer replaces them with the Unicode replacement character (`"\u{FFFD}"`).

## Parameters

- `nullTerminatedCodeUnits`: A pointer to a null-terminated sequence of   code units encoded in  .
- `encoding`: The encoding in which the code units should be   interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(decodingcstring:as:)-8yowf)*