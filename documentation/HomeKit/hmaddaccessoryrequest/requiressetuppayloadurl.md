# requiresSetupPayloadURL

**Framework**: HomeKit  
**Kind**: property

An indication of whether the add operation requires a setup payload URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
var requiresSetupPayloadURL: Bool { get }
```

#### Discussion

If this value is `true`, look up the URL for the given accessory based on its category and name, given by the request’s [`accessoryCategory`](hmaddaccessoryrequest/accessorycategory.md) and [`accessoryName`](hmaddaccessoryrequest/accessoryname.md) parameters. Include the URL in the setup payload by calling the request’s [`makePayload(url:ownershipToken:)`](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md) method.

If [`requiresSetupPayloadURL`](hmaddaccessoryrequest/requiressetuppayloadurl.md) is `false`, you can still use the [`makePayload(url:ownershipToken:)`](hmaddaccessoryrequest/makepayload(url:ownershiptoken:).md) method, if appropriate. Alternatively, you can construct the payload by calling the request’s [`makePayload(ownershipToken:)`](hmaddaccessoryrequest/makepayload(ownershiptoken:).md) command instead.

## See Also

- [var home: HMHome](hmaddaccessoryrequest/home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](hmaddaccessoryrequest/accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](hmaddaccessoryrequest/accessoryname.md)
  The name of the accessory to add.
- [var requiresOwnershipToken: Bool](hmaddaccessoryrequest/requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/requiressetuppayloadurl)*