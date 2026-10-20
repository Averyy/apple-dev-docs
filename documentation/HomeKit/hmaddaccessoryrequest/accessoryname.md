# accessoryName

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name of the accessory to add.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
var accessoryName: String { get }
```

```objc
@property (nonatomic, readonly) NSString * accessoryName;
```

## See Also

### Characterizing the Request
- [var home: HMHome](./home.md)
  The home to which to add the accessory.
- [var accessoryCategory: HMAccessoryCategory](./accessorycategory.md)
  The category of the accessory to add.
- [var requiresOwnershipToken: Bool](./requiresownershiptoken.md)
  An indication of whether the add operation requires an ownership token.
- [var requiresSetupPayloadURL: Bool](./requiressetuppayloadurl.md)
  An indication of whether the add operation requires a setup payload URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaddaccessoryrequest/accessoryname)*