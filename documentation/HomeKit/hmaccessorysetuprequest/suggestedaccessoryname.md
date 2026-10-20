# suggestedAccessoryName

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name that the framework suggests when the user names the accessory being set up.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 27.0+

## Declaration

```swift
var suggestedAccessoryName: String? { get set }
```

```objc
@property (copy, nullable) NSString * suggestedAccessoryName;
```

#### Discussion

If this value is `nil`, then the suggested name is taken from the accessory itself. If the user sets up an accessory bridge, then this value only applies to the accessory bridge and not any accessories behind the bridge.

## See Also

### Setting up accessorices
- [var homeUniqueIdentifier: UUID?](./homeuniqueidentifier.md)
  The identifier corresponding to the home that the accessory should be added to when being set up.
- [var payload: HMAccessorySetupPayload?](./payload.md)
  The payload to use for accessory setup.
- [var suggestedRoomUniqueIdentifier: UUID?](./suggestedroomuniqueidentifier.md)
  The identifier corresponding to the room that the framework suggests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessorysetuprequest/suggestedaccessoryname)*