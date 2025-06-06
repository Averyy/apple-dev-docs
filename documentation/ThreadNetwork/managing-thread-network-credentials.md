# Managing Thread network credentials

**Framework**: ThreadNetwork

Store, delete, retrieve, and update Thread network credentials on your Apple device.

#### Overview

Thread network credentials reside in iCloud Keychain, where your app manages and protects them. You must keep credentials for all your Border Routers up to date to protect the network’s resiliency.

##### Store and Delete Credentials

When a Border Router joins the Thread network, use [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md) to store or update the credentials to iCloud Keychain. When a Border Router leaves the Thread network, use [`deleteCredentials(forBorderAgent:completion:)`](thclient/deletecredentials(forborderagent:completion:).md) to remove the credentials from iCloud Keychain.

##### Retrieve the Preferred Network Credentials

Retrieving preferred network credentials requires user consent. Before asking for user consent, verify that the preferred network is configured by calling [`isPreferredNetworkAvailable(completion:)`](thclient/ispreferrednetworkavailable(completion:).md).

> **Note**: Retrieving preferred network credentials requires user consent.

Retrieving preferred network credentials requires user consent.

If you have previously cached preferred network credentials, call [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md) to verify that they match the preferred network credentials. If they don’t match, retrieve the preferred network credentials using [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md).

##### Retrieve Your Own Credentials

You can retrieve credentials for a single Border Router using [`retrieveCredentials(forBorderAgent:completion:)`](thclient/retrievecredentials(forborderagent:completion:).md). To retrieve credentials for all of your Border Routers, use [`retrieveAllCredentials(_:)`](thclient/retrieveallcredentials(_:).md). If you only want to read the active  Border Router’s credentials, use [`retrieveAllActiveCredentials(_:)`](thclient/retrieveallactivecredentials(_:).md). Retrieving records with these methods doesn’t require user consent.

##### Update Your Border Router with Preferred Network Credentials

If your Border Router is already on the preferred network, use [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md) at app launch to determine if there are any modifications to the preferred network credentials. If there are, use [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md) to read the updated preferred network credentials and store them to iCloud Keychain. This ensures that your Border Router’s credentials always match the preferred network credentials.

##### Update the Preferred Network with Border Router Credentials

If your app detects a modification to the Thread credentials of a configured Border Router, update the credentials on iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md).

> ❗ **Important**: When you store your Border Router credentials to iCloud Keychain using the Border Agent ID, that ID becomes a part of the preferred network. Any modifications that the Border Router makes using that Border Agent ID also modifies the preferred network credentials in iCloud Keychain.

When you store your Border Router credentials to iCloud Keychain using the Border Agent ID, that ID becomes a part of the preferred network. Any modifications that the Border Router makes using that Border Agent ID also modifies the preferred network credentials in iCloud Keychain.

If you want to change your Border Router credentials without affecting the preferred network credentials, delete the existing credentials in iCloud Keychain and then store the new credentials with a new Border Agent ID.

##### Detect a Modified Ssid

If a person changes the SSID of a Thread-capable Wi-Fi router, confirm that the credentials match the preferred network credentials with [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md). If not, read the preferred network credentials using [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md) and store them in iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md).

## See Also

- [Configuring a Border Router](configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/managing-thread-network-credentials)*