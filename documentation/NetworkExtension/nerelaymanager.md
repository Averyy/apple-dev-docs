# NERelayManager

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object you use to create and manage a network relay configuration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NERelayManager
```

```objc
@interface NERelayManager : NSObject
```

#### Overview

When your app starts up, access the shared instance of the relay manager, and load existing settings from the preferences using [`loadFromPreferences(completionHandler:)`](./nerelaymanager/loadfrompreferences%28completionhandler%29.md). You can define your relay server configuration, and persist it by calling [`saveToPreferences(completionHandler:)`](./nerelaymanager/savetopreferences%28completionhandler%29.md).

## Topics

### Managing relay configurations
- [class func shared() -> NERelayManager](./nerelaymanager/shared%28%29.md)
  Access the single instance of a network relay manager.
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](./nerelaymanager/loadfrompreferences%28completionhandler%29.md)
  Load your relay configuration from the system networking preferences.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](./nerelaymanager/savetopreferences%28completionhandler%29.md)
  Save your relay configuration to the system networking preferences.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](./nerelaymanager/removefrompreferences%28completionhandler%29.md)
  Remove your relay configuration from the system networking preferences.
### Accessing relay configuration properties
- [var isEnabled: Bool](./nerelaymanager/isenabled.md)
  A Boolean used to toggle the enabled state of the relay configuration.
- [var relays: [NERelay]?](./nerelaymanager/relays.md)
  An array of one or two relay server configurations. If multiple relays are configured, application traffic routes through both of them in the order they appear in the array.
- [var matchDomains: [String]?](./nerelaymanager/matchdomains.md)
  A list of domain strings used to determine which connections will use the relay configuration contained in this object.
- [var excludedDomains: [String]?](./nerelaymanager/excludeddomains.md)
  A list of domain strings used to determine which connections won’t use the relay configuration contained in this object.
- [var localizedDescription: String?](./nerelaymanager/localizeddescription.md)
  A string that contains the display name of the relay configuration.
- [var onDemandRules: [NEOnDemandRule]?](./nerelaymanager/ondemandrules.md)
  An array of rules you use to determine which networks the relay uses.
- [class NEOnDemandRule](./neondemandrule.md)
  A base class shared by all VPN On Demand rules.
### Loading previously-used managers
- [class func loadAllManagersFromPreferences(completionHandler: ([NERelayManager], (any Error)?) -> Void)](./nerelaymanager/loadallmanagersfrompreferences%28completionhandler%29.md)
  Asynchronously reads all the relay configurations previously created and saved by the calling app.
### Handling errors
- [let NERelayErrorDomain: String](./nerelayerrordomain.md)
  The domain for errors resulting from calls to the relay manager.
- [enum NERelayManagerError](./nerelaymanagererror.md)
  Error codes specific to relay managers.
### Instance Properties
- [var excludedFQDNs: [String]?](./nerelaymanager/excludedfqdns.md)
- [var isDNSFailoverAllowed: Bool](./nerelaymanager/isdnsfailoverallowed.md)
- [var isUIToggleEnabled: Bool](./nerelaymanager/isuitoggleenabled.md)
- [var matchFQDNs: [String]?](./nerelaymanager/matchfqdns.md)
### Instance Methods
- [func getLastClientErrors(TimeInterval, completionHandler: ([any Error]?) -> Void)](./nerelaymanager/getlastclienterrors%28_,completionhandler%29.md)

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

## See Also

### Relay configuration
- [class NERelay](./nerelay.md)
  A single relay server configuration that you can chain together with other relays.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nerelaymanager)*