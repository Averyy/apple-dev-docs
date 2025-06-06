# init(decodingCString:as:)

**Framework**: Swift  
**Kind**: init  
**Required**: Yes

Creates a string from the null-terminated sequence of bytes at the given pointer.

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
init<Encoding>(decodingCString nullTerminatedCodeUnits: UnsafePointer<Encoding.CodeUnit>, as sourceEncoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

## Parameters

- `nullTerminatedCodeUnits`: A pointer to a sequence of contiguous code   units in the encoding specified in  , ending just   before the first zero code unit.
- `sourceEncoding`: The encoding in which the code units should be   interpreted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/init(decodingcstring:as:))*