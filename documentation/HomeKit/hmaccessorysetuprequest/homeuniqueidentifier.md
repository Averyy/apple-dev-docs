# homeUniqueIdentifier

**Framework**: HomeKit  
**Kind**: property

The identifier corresponding to the home that the accessory should be added to when being set up.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+

## Declaration

```swift
var homeUniqueIdentifier: UUID? { get set }
```

#### Discussion

If `nil`, then the user chooses a home. See [`uniqueIdentifier`](hmhome/uniqueidentifier.md) for more information.

## See Also

- [var payload: HMAccessorySetupPayload?](hmaccessorysetuprequest/payload.md)
  The payload to use for accessory setup.
- [var suggestedAccessoryName: String?](hmaccessorysetuprequest/suggestedaccessoryname.md)
  The name that the framework suggests when the user names the accessory being set up.
- [var suggestedRoomUniqueIdentifier: UUID?](hmaccessorysetuprequest/suggestedroomuniqueidentifier.md)
  The identifier corresponding to the room that the framework suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest/homeuniqueidentifier)*