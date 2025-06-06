# init(url:)

**Framework**: HomeKit  
**Kind**: init

Creates an accessory setup payload.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- visionOS 1.0+

## Declaration

```swift
init?(url setupPayloadURL: URL?)
```

#### Discussion

For details about the payload’s content, please join the [`MFi Program`](https://developer.apple.comhttps://developer.apple.com/programs/mfi/).

## Parameters

- `setupPayloadURL`: The payload used to securely authenticate the accessory. This is the same payload you would receive by scanning the accessory’s QR code.

## See Also

- [init?(url: URL, ownershipToken: HMAccessoryOwnershipToken?)](hmaccessorysetuppayload/init(url:ownershiptoken:).md)
  Creates an accessory setup payload instance that includes an ownership token.
- [class HMAccessoryOwnershipToken](hmaccessoryownershiptoken.md)
  Authentication data that your app provides when adding an accessory to a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload/init(url:))*