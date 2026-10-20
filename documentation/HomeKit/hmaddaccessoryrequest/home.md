# home

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The home to which to add the accessory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
var home: HMHome { get }
```

```objc
@property (nonatomic, strong, readonly) HMHome * home;
```

#### Discussion

Call this home’s [`addAndSetupAccessories(with:completionHandler:)`](../hmhome/addandsetupaccessories%28with,completionhandler%29.md) method to fulfill the request after constructing the setup payload.

## See Also

### Characterizing the Request
- [var accessoryCategory: HMAccessoryCategory](./accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](./accessoryname.md)
  The name of the accessory to add.
- [var requiresOwnershipToken: Bool](./requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.
- [var requiresSetupPayloadURL: Bool](./requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/home)*