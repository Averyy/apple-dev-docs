# THClient

**Framework**: ThreadNetwork  
**Kind**: class

A class that supports safely sharing Thread credentials between multiple clients.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class THClient
```

#### Overview

Request credentials for either a specific Thread network or for the  using [`THClient`](thclient.md). The preferred network is the default Thread network chosen by the framework for a home.

The ThreadNetwork framework maintains a database of network credentials. The class allows clients to store, list, and delete credentials for a given network from the database.

Some methods in [`THClient`](thclient.md) use the , a string that you store in your application’s `Info.plist`. The ThreadNetwork framework uses the team ID to preserve the privacy of the Thread network credentials across different clients. For example, credentials stored by one client can’t be deleted or modified by another client.

> ❗ **Important**: Thread credentials give you the ability to add any device into the Thread network. Use this information responsibly.

Thread credentials give you the ability to add any device into the Thread network. Use this information responsibly.

## Topics

### Creating the Client
- [init()](thclient/init.md)
  Creates the client object.
### Retrieving Credentials
- [func isPreferredNetworkAvailable(completion: (Bool) -> Void)](thclient/ispreferrednetworkavailable(completion:).md)
  Indicates whether a preferred network is available.
- [func checkPreferredNetwork(forActiveOperationalDataset: Data, completion: (Bool) -> Void)](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md)
  Determines if the essential operating parameters match the preferred network’s parameters.
- [func retrieveCredentials(forBorderAgent: Data, completion: (THCredentials?, (any Error)?) -> Void)](thclient/retrievecredentials(forborderagent:completion:).md)
  Requests Thread credentials for a Border Agent.
- [func retrieveCredentials(forExtendedPANID: Data, completion: (THCredentials?, (any Error)?) -> Void)](thclient/retrievecredentials(forextendedpanid:completion:).md)
  Requests Thread credentials for an extended Personal Area Network (PAN) ID.
- [func retrieveAllCredentials((Set<THCredentials>?, (any Error)?) -> Void)](thclient/retrieveallcredentials(_:).md)
  Requests all Thread credentials from the framework.
- [func retrievePreferredCredentials((THCredentials?, (any Error)?) -> Void)](thclient/retrievepreferredcredentials(_:).md)
  Requests Thread credentials for the preferred network.
- [func retrieveAllActiveCredentials((Set<THCredentials>?, (any Error)?) -> Void)](thclient/retrieveallactivecredentials(_:).md)
  Returns a set of the active credentials.
### Storing and Deleting Credentials
- [func deleteCredentials(forBorderAgent: Data, completion: ((any Error)?) -> Void)](thclient/deletecredentials(forborderagent:completion:).md)
  Deletes Thread network credentials from the framework database for a Border Agent.
- [func storeCredentials(forBorderAgent: Data, activeOperationalDataSet: Data, completion: ((any Error)?) -> Void)](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md)
  Stores Thread network credentials into the framework database that a Border Agent provides.

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

- [com.apple.developer.networking.manage-thread-network-credentials](../BundleResources/Entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [class THCredentials](thcredentials.md)
  A class that contains credentials for a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/thclient)*