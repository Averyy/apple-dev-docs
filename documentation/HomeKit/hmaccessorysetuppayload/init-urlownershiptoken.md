# init(url:ownershipToken:)

**Framework**: HomeKit  
**Kind**: init

Creates an accessory setup payload instance that includes an ownership token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(url setupPayloadURL: URL, ownershipToken: HMAccessoryOwnershipToken?)
```

#### Discussion

For details about the payload’s content, join the [`MFi Program`](https://developer.apple.comhttps://developer.apple.com/programs/mfi/).

## Parameters

- `setupPayloadURL`: The payload used to securely authenticate the accessory. This is the same payload you would receive by scanning the accessory’s QR code.
- `ownershipToken`: A token that proves ownership of the accessory. You typically negotiate this token with the accessory outside of HomeKit.

## See Also

- [init?(url: URL?)](hmaccessorysetuppayload/init(url:).md)
  Creates an accessory setup payload.
- [class HMAccessoryOwnershipToken](hmaccessoryownershiptoken.md)
  Authentication data that your app provides when adding an accessory to a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuppayload/init(url:ownershiptoken:))*