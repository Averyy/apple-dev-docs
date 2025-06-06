# makePayload(url:ownershipToken:)

**Framework**: HomeKit  
**Kind**: method

Builds an accessory setup payload with the given setup payload URL and ownership token.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func makePayload(url setupPayloadURL: URL, ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?
```

#### Return Value

An accessory setup payload that you use to add the accessory. The method fails and returns `nil` if the setup payload URL is invalid.

## Parameters

- `setupPayloadURL`: The setup payload URL for the accessory. Provide this URL when HomeKit sends an add request to the app associated with your accessory. You determine the URL based on the category and name of your accessory, as given in the   and   properties of the associated   instance.
- `ownershipToken`: A token proving ownership of the accessory. Your app negotiates the token with the accessory outside of HomeKit.

## See Also

- [func makePayload(ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?](hmaddaccessoryrequest/makepayload(ownershiptoken:).md)
  Builds an accessory setup payload with the given ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/makepayload(url:ownershiptoken:))*