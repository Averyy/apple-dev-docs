# payload

**Framework**: HomeKit  
**Kind**: property

The payload to use for accessory setup.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Declaration

```swift
@NSCopying
var payload: HMAccessorySetupPayload? { get set }
```

#### Discussion

See [`HMAccessorySetupPayload`](hmaccessorysetuppayload.md) for more information.

## See Also

- [var homeUniqueIdentifier: UUID?](hmaccessorysetuprequest/homeuniqueidentifier.md)
  The identifier corresponding to the home that the accessory should be added to when being set up.
- [var suggestedAccessoryName: String?](hmaccessorysetuprequest/suggestedaccessoryname.md)
  The name that the framework suggests when the user names the accessory being set up.
- [var suggestedRoomUniqueIdentifier: UUID?](hmaccessorysetuprequest/suggestedroomuniqueidentifier.md)
  The identifier corresponding to the room that the framework suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest/payload)*