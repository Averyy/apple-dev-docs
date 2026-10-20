# generalCardData

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

A Base64-encoded string that contains general cardholder and terminal data in tag-length-value (TLV) format.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let generalCardData: String?
```

#### Discussion

The content of this field is determined by your payment service provider. This field can contain both card tags and terminal tags.

## See Also

### Getting the result data
- [let paymentCardData: String?](./paymentcarddata.md)
  A Base64-encoded string that contains the encrypted payment information to send to your payment provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/generalcarddata)*