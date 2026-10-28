# suggestedRoomUniqueIdentifier

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The identifier corresponding to the room that the framework suggests.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
var suggestedRoomUniqueIdentifier: UUID? { get set }
```

```objc
@property (copy, nullable) NSUUID * suggestedRoomUniqueIdentifier;
```

## Discussion

If `nil`, then any room may be suggested. See [`uniqueIdentifier`](../hmhome/uniqueidentifier.md) for more information.

## See Also

### Setting up accessorices
- [var homeUniqueIdentifier: UUID?](./homeuniqueidentifier.md)
  The identifier corresponding to the home that the accessory should be added to when being set up.
- [var payload: HMAccessorySetupPayload?](./payload.md)
  The payload to use for accessory setup.
- [var suggestedAccessoryName: String?](./suggestedaccessoryname.md)
  The name that the framework suggests when the user names the accessory being set up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest/suggestedroomuniqueidentifier)*