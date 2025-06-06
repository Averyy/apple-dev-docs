# home

**Framework**: HomeKit  
**Kind**: property

The home to which to add the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
var home: HMHome { get }
```

#### Discussion

Call this home’s [`addAndSetupAccessories(with:completionHandler:)`](hmhome/addandsetupaccessories(with:completionhandler:).md) method to fulfill the request after constructing the setup payload.

## See Also

- [var accessoryCategory: HMAccessoryCategory](hmaddaccessoryrequest/accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](hmaddaccessoryrequest/accessoryname.md)
  The name of the accessory to add.
- [var requiresOwnershipToken: Bool](hmaddaccessoryrequest/requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.
- [var requiresSetupPayloadURL: Bool](hmaddaccessoryrequest/requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/home)*