# makePayload(ownershipToken:)

**Framework**: HomeKit  
**Kind**: method

Builds an accessory setup payload with the given ownership token.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func makePayload(ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?
```

#### Return Value

An accessory setup payload that you use to add the accessory. The method fails and returns `nil` if the request’s [`requiresSetupPayloadURL`](hmaddaccessoryrequest/requiressetuppayloadurl.md) property is `true`. In that case, use [`makePayload(url:ownershipToken:)`](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md) instead.

## Parameters

- `ownershipToken`: A token proving ownership of the accessory.

## See Also

- [func makePayload(url: URL, ownershipToken: HMAccessoryOwnershipToken) -> HMAccessorySetupPayload?](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md)
  Builds an accessory setup payload with the given setup payload URL and ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/makepayload(ownershiptoken:))*