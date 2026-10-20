# payload

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The payload to use for accessory setup.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
@NSCopying
var payload: HMAccessorySetupPayload? { get set }
```

```objc
@property (copy, nullable) HMAccessorySetupPayload * payload;
```

#### Discussion

See [`HMAccessorySetupPayload`](../hmaccessorysetuppayload.md) for more information.

## See Also

### Setting up accessorices
- [var homeUniqueIdentifier: UUID?](./homeuniqueidentifier.md)
  The identifier corresponding to the home that the accessory should be added to when being set up.
- [var suggestedAccessoryName: String?](./suggestedaccessoryname.md)
  The name that the framework suggests when the user names the accessory being set up.
- [var suggestedRoomUniqueIdentifier: UUID?](./suggestedroomuniqueidentifier.md)
  The identifier corresponding to the room that the framework suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest/payload)*