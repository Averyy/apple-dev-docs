# session(_:didGenerateShareableConfigurationData:for:)

**Framework**: Nearby Interaction  
**Kind**: method  
**Role**: Instance Method

Provides configuration data to share with a third-party accessory.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- watchOS 8.0+

## Declaration

```swift
optional func session(_ session: NISession, didGenerateShareableConfigurationData shareableConfigurationData: Data, for object: NINearbyObject)
```

```objc
- (void) session:(NISession *) session didGenerateShareableConfigurationData:(NSData *) shareableConfigurationData forObject:(NINearbyObject *) object;
```

## Mentions

- [Initiating and maintaining a session](../initiating-and-maintaining-a-session.md)

## Discussion

The system invokes this callback only for sessions that run an accessory configuration. The `shareableConfigurationData` argument contains information that the accessory needs to begin the session. For more information, see [`NINearbyAccessoryConfiguration`](../ninearbyaccessoryconfiguration.md).

## Parameters

- `session`: The session that produced the configuration data.
- `shareableConfigurationData`: The data to share with the accessory.
- `object`: A representation of the accessory as an [`NINearbyObject`](../ninearbyobject.md).

## See Also

### Monitoring peers
- [func session(NISession, didUpdate: [NINearbyObject])](./session%28_,didupdate%29.md)
  Notifies you when the session updates nearby objects.
- [func session(NISession, didRemove: [NINearbyObject], reason: NINearbyObject.RemovalReason)](./session%28_,didremove,reason%29.md)
  Notifies you when the session removes one or more nearby objects.
- [NINearbyObject.RemovalReason](../ninearbyobject/removalreason.md)
  The reason a session removed a nearby object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didgenerateshareableconfigurationdata:for:))*