# SMSMessageID.RawValue

**Framework**: TelephonyMessagingKit  
**Kind**: typealias

The raw type that can be used to represent all values of the conforming type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
typealias RawValue = UInt32
```

#### Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.

## See Also

- [let rawValue: UInt32](smsmessageid/rawvalue-swift.property.md)
  The identifier of an SMS message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/smsmessageid/rawvalue-swift.typealias)*