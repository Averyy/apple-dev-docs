# requiresOwnershipToken

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An indication of whether the add operation requires an ownership token.

**Availability**:
- iOS 13.0+ - Deprecated in 13.0
- iPadOS 13.0+ - Deprecated in 13.0
- Mac Catalyst 13.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported

## Declaration

```swift
var requiresOwnershipToken: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL requiresOwnershipToken;
```

#### Discussion

In practice, this value is always `true`.

## See Also

### Characterizing the Request
- [var home: HMHome](./home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](./accessorycategory.md)
  The category of the accessory to add.
- [var accessoryName: String](./accessoryname.md)
  The name of the accessory to add.
- [var requiresSetupPayloadURL: Bool](./requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/requiresownershiptoken)*