# argumentStringValue

**Framework**: OSLog  
**Kind**: property

The argument formatted as a string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var argumentStringValue: String? { get }
```

#### Discussion

The `argumentStringValue` property can be `nil` if the argument can’t be decoded. For example, redacted arguments or the last component can’t be decoded.

## See Also

- [var argumentDataValue: Data?](oslogmessagecomponent/argumentdatavalue.md)
  The argument formatted as a sequence of bytes.
- [var argumentDoubleValue: Double](oslogmessagecomponent/argumentdoublevalue.md)
  The argument formatted as a double.
- [var argumentInt64Value: Int64](oslogmessagecomponent/argumentint64value.md)
  The argument formatted as a signed 64-bit integer.
- [var argumentNumberValue: NSNumber?](oslogmessagecomponent/argumentnumbervalue.md)
  The argument formatted as a number.
- [var argumentUInt64Value: UInt64](oslogmessagecomponent/argumentuint64value.md)
  The argument formatted as an unsigned 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogmessagecomponent/argumentstringvalue)*