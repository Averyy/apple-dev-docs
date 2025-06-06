# NEAppPushManager

**Framework**: Network Extension  
**Kind**: class

An object that configures a push provider and manages its life cycle.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class NEAppPushManager
```

## Mentions

- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)

#### Overview

Your app can create as many [`NEAppPushManager`](neapppushmanager.md) instances as you need. Load your managers from the persistent store and set up their delegates immediately after the app launches, so they’re ready to handle incoming calls.

## Topics

### Matching Wi-Fi networks
- [var matchSSIDs: [String]](neapppushmanager/matchssids.md)
  An array of Wi-Fi SSID strings that the system matches for local push activation.
- [var matchPrivateLTENetworks: [NEPrivateLTENetwork]](neapppushmanager/matchprivateltenetworks.md)
  An array of private LTE networks that the system matches for local push activation.
- [class NEPrivateLTENetwork](neprivateltenetwork.md)
  The parameters of a private LTE network.
### Persisting manager settings
- [func loadFromPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/loadfrompreferences(completionhandler:).md)
  Loads the manager’s saved configuration from the persistent store.
- [class func loadAllFromPreferences(completionHandler: ([NEAppPushManager]?, (any Error)?) -> Void)](neapppushmanager/loadallfrompreferences(completionhandler:).md)
  Loads all saved manager configurations asynchronously.
- [func saveToPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/savetopreferences(completionhandler:).md)
  Saves the manager’s configuration in the persistent store.
- [func removeFromPreferences(completionHandler: ((any Error)?) -> Void)](neapppushmanager/removefrompreferences(completionhandler:).md)
  Removes the manager’s configuration from the persistent store.
### Working with a delegate
- [var delegate: (any NEAppPushDelegate)?](neapppushmanager/delegate.md)
  A delegate that receives incoming call information from the provider.
- [protocol NEAppPushDelegate](neapppushdelegate.md)
  A protocol that defines how an app push manager instance interacts with the framework.
### Inspecting manager properties
- [var isActive: Bool](neapppushmanager/isactive.md)
  A Boolean value that indicates whether a configuration is in use.
- [var isEnabled: Bool](neapppushmanager/isenabled.md)
  A property you use to toggle enabling the configuration.
- [var localizedDescription: String?](neapppushmanager/localizeddescription.md)
  A string that contains the localized description of the app push manager.
### Inspecting provider properties
- [var providerConfiguration: [String : Any]](neapppushmanager/providerconfiguration.md)
  A dictionary that contains vendor-specific key-value pairs, that you use to configure a provider.
- [var providerBundleIdentifier: String?](neapppushmanager/providerbundleidentifier.md)
  A string that contains the bundle identifier of the push provider.
### Handling errors
- [struct NEAppPushManagerError](neapppushmanagererror-swift.struct.md)
  An error that the push manager encounters.
- [let NEAppPushErrorDomain: String](neapppusherrordomain.md)
  The error domain string for local push errors.
- [NEAppPushManagerError.Code](neapppushmanagererror-swift.struct/code.md)
  Error codes that the local push API declares.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppPushProvider](neapppushprovider.md)
  An object that creates and maintains a persistent network connection to a local push server.
- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)
  Implement your Local Push Connectivity app to ensure delivery of notifications.
- [Receiving Voice and Text Communications on a Local Network](receiving-voice-and-text-communications-on-a-local-network.md)
  Provide voice and text communication on a local network isolated from Apple Push Notification service by adopting Local Push Connectivity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager)*