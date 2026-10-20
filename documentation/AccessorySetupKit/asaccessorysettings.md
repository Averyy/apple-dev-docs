# ASAccessorySettings

**Framework**: AccessorySetupKit  
**Kind**: class  
**Role**: Class

Properties of an accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
class ASAccessorySettings
```

```objc
@interface ASAccessorySettings : NSObject
```

## Topics

### Applying default settings
- [class var `default`: ASAccessorySettings](./asaccessorysettings/default.md)
  An empty settings object.
### Inspecting accessory settings
- [var ssid: String?](./asaccessorysettings/ssid.md)
  A hotspot identifier that clients can use to connect to an accessory’s hotspot.
- [var bluetoothTransportBridgingIdentifier: Data?](./asaccessorysettings/bluetoothtransportbridgingidentifier.md)
  A 6-byte identifier for bridging classic transport profiles.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing authorization
- [func finishAuthorization(for: ASAccessory, settings: ASAccessorySettings, completionHandler: ((any Error)?) -> Void)](./asaccessorysession/finishauthorization%28for,settings,completionhandler%29.md)
  Finish authorization of a partially-setup accessory.
- [func failAuthorization(for: ASAccessory, completionHandler: ((any Error)?) -> Void)](./asaccessorysession/failauthorization%28for,completionhandler%29.md)
  End authorization of a partially-configured accessory as a failure.
- [func updateAuthorization(for: ASAccessory, descriptor: ASDiscoveryDescriptor, completionHandler: ((any Error)?) -> Void)](./asaccessorysession/updateauthorization%28for,descriptor,completionhandler%29.md)
  Displays a view to upgrade an accessory with additional technology permissions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessorysettings)*