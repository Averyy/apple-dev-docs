# Managing Thread network credentials

**Framework**: ThreadNetwork

Store, retrieve, update, and delete Thread network credentials on your Apple device.

#### Overview

Your app stores Thread network credentials in iCloud Keychain, where the system manages and protects them. You need to keep credentials for all your Border Routers up to date to protect the network’s resiliency.

##### Store and Delete Credentials

When a Thread Border Router joins the Thread network, use [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md) to store or update the credentials to iCloud Keychain. When a Thread Border Router leaves the Thread network, use [`deleteCredentials(forBorderAgent:completion:)`](thclient/deletecredentials(forborderagent:completion:).md) to remove the credentials from iCloud Keychain.

##### Retrieve the Preferred Network Credentials

Retrieving preferred network credentials requires a person’s consent. Before asking for a person’s consent, verify that the preferred network is configured by calling [`isPreferredNetworkAvailable(completion:)`](thclient/ispreferrednetworkavailable(completion:).md).

> **Note**: Retrieving preferred network credentials requires a person’s’ consent.

If you’ve previously cached preferred network credentials, call [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md) to verify that they match the preferred network credentials. If they don’t match, retrieve the preferred network credentials using [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md).

##### Retrieve Your Own Credentials

You can retrieve credentials for a single Thread Border Router using [`retrieveCredentials(forBorderAgent:completion:)`](thclient/retrievecredentials(forborderagent:completion:).md). To retrieve credentials for all of your Thread Border Routers, use [`retrieveAllCredentials(_:)`](thclient/retrieveallcredentials(_:).md). If you only want to read the active Thread Border Router’s credentials, use [`retrieveAllActiveCredentials(_:)`](thclient/retrieveallactivecredentials(_:).md). Retrieving records with these methods doesn’t require a person’s consent.

##### Update Your Thread Border Router with Preferred Network Credentials

If your Thread Border Router is already on the preferred network, use [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md) at app launch to determine if there are any modifications to the preferred network credentials. If there are, use [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md) to read the updated preferred network credentials and store them to iCloud Keychain. This ensures that your Thread Border Router’s credentials always match the preferred network credentials.

##### Update the Preferred Network with Thread Border Router Credentials

If your app detects a modification to the Thread credentials of a configured Border Router, update the credentials on iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md).

> ❗ **Important**: When you store your Thread Border Router credentials to iCloud Keychain using the Border Agent ID, that ID becomes a part of the preferred network. Any modifications that the Thread Border Router makes using that Border Agent ID also modifies the preferred network credentials in iCloud Keychain.

If you want to change your Thread Border Router credentials without affecting the preferred network credentials, delete the existing credentials in iCloud Keychain and then store the new credentials with a new Border Agent ID.

##### Detect a Modified Service Set Identifier Ssid

If a person changes the SSID of a Thread-capable Wi-Fi router, confirm that the credentials match the preferred network credentials with [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](thclient/checkpreferrednetwork(foractiveoperationaldataset:completion:).md). If not, read the preferred network credentials using [`retrievePreferredCredentials(_:)`](thclient/retrievepreferredcredentials(_:).md) and store them in iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](thclient/storecredentials(forborderagent:activeoperationaldataset:completion:).md).

## See Also

- [Getting started with ThreadNetwork](getting-started-with-threadnetwork.md)
  Create a plan to build, test, and deploy your Thread Border Router app.
- [Configuring a Border Router](configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/managing-thread-network-credentials)*