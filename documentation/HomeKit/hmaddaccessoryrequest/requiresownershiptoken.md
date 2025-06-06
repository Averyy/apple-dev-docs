# requiresOwnershipToken

**Framework**: HomeKit  
**Kind**: property

An indication of whether the add operation requires an ownership token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var requiresOwnershipToken: Bool { get }
```

#### Discussion

In practice, this value is always `true`.

## See Also

- [var home: HMHome](hmaddaccessoryrequest/home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](hmaddaccessoryrequest/accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](hmaddaccessoryrequest/accessoryname.md)
  The name of the accessory to add.
- [var requiresSetupPayloadURL: Bool](hmaddaccessoryrequest/requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/requiresownershiptoken)*