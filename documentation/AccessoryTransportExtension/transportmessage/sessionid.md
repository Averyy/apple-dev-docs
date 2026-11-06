# sessionID

**Framework**: Accessory Transport Extension  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the feature to which the message belongs.

**Availability**:
- iOS 26.5+

## Declaration

```swift
let sessionID: UUID
```

## Mentions

- [Forwarding notifications to your accessory using the internet transport type](../forwarding-notifications-to-your-accessory-using-the-internet-transport-type.md)

## Discussion

This identifier specifies the feature to which an incoming message belongs. It’s the feature ID your accessory uses when it derives encryption secrets. For internet transport, your accessory also includes the identifier in responses to help the system deliver them to the correct data provider extension. It isn’t the same value as [`featureID`](../accessoryfeature/featureid.md), which names a feature type. The value is fixed while the accessory remains paired through AccessorySetupKit.

## See Also

### Accessing message content
- [let data: Data](./data.md)
  A data object that contains the message content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/transportmessage/sessionid)*