# requiresSetupPayloadURL

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An indication of whether the add operation requires a setup payload URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
var requiresSetupPayloadURL: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL requiresSetupPayloadURL;
```

#### Discussion

If this value is `true`, look up the URL for the given accessory based on its category and name, given by the request’s [`accessoryCategory`](./accessorycategory.md) and [`accessoryName`](./accessoryname.md) parameters. Include the URL in the setup payload by calling the request’s [`makePayload(url:ownershipToken:)`](./makepayload%28url,ownershiptoken%29.md) method.

If [`requiresSetupPayloadURL`](./requiressetuppayloadurl.md) is `false`, you can still use the [`makePayload(url:ownershipToken:)`](./makepayload%28url,ownershiptoken%29.md) method, if appropriate. Alternatively, you can construct the payload by calling the request’s [`makePayload(ownershipToken:)`](./makepayload%28ownershiptoken%29.md) command instead.

## See Also

### Characterizing the Request
- [var home: HMHome](./home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](./accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](./accessoryname.md)
  The name of the accessory to add.
- [var requiresOwnershipToken: Bool](./requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/requiressetuppayloadurl)*