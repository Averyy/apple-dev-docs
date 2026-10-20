# argumentDataValue

**Framework**: OSLog  
**Kind**: property  
**Role**: Instance Property

The argument formatted as a sequence of bytes.

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
var argumentDataValue: Data? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSData * argumentDataValue;
```

#### Discussion

The `argumentDataValue` property can be `nil` if the argument can’t be decoded. For example, redacted arguments and the last component can’t be decoded.

## See Also

### Accessing the Argument
- [var argumentDoubleValue: Double](./argumentdoublevalue.md)
  The argument formatted as a double.
- [var argumentInt64Value: Int64](./argumentint64value.md)
  The argument formatted as a signed 64-bit integer.
- [var argumentNumberValue: NSNumber?](./argumentnumbervalue.md)
  The argument formatted as a number.
- [var argumentStringValue: String?](./argumentstringvalue.md)
  The argument formatted as a string.
- [var argumentUInt64Value: UInt64](./argumentuint64value.md)
  The argument formatted as an unsigned 64-bit integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogmessagecomponent/argumentdatavalue)*