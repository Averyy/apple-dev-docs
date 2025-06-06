# string(fromByteCount:countStyle:)

**Framework**: Foundation  
**Kind**: method

Converts a byte count into the specified string format without creating an `NSNumber` object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func string(fromByteCount byteCount: Int64, countStyle: ByteCountFormatter.CountStyle) -> String
```

#### Return Value

A string containing the formatted `byteCount` value.

## Parameters

- `byteCount`: The byte count.
- `countStyle`: The formatter style. See   for possible values.

## See Also

- [Data Formatting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [func string(fromByteCount: Int64) -> String](bytecountformatter/string(frombytecount:).md)
  Converts a byte count into a string without creating an `NSNumber` object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter/string(frombytecount:countstyle:))*