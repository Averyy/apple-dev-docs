# Managing Thread network credentials

**Framework**: ThreadNetwork  
**Role**: Article

Store, retrieve, update, and delete Thread network credentials on your Apple device.

#### Overview

Your app stores Thread network credentials in iCloud Keychain, where the system manages and protects them. You need to keep credentials for all your Border Routers up to date to protect the network’s resiliency.

##### Store and delete credentials

When a Thread Border Router joins the Thread network, use [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](./thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md) to store or update the credentials to iCloud Keychain. When a Thread Border Router leaves the Thread network, use [`deleteCredentials(forBorderAgent:completion:)`](./thclient/deletecredentials%28forborderagent,completion%29.md) to remove the credentials from iCloud Keychain.

##### Retrieve the preferred network credentials

Retrieving preferred network credentials requires a person’s consent. Before asking for a person’s consent, verify that the preferred network is configured by calling [`isPreferredNetworkAvailable(completion:)`](./thclient/ispreferrednetworkavailable%28completion%29.md).

> **Note**: Retrieving preferred network credentials requires a person’s’ consent.

If you’ve previously cached preferred network credentials, call [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](./thclient/checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md) to verify that they match the preferred network credentials. If they don’t match, retrieve the preferred network credentials using [`retrievePreferredCredentials(_:)`](./thclient/retrievepreferredcredentials%28_%29.md).

##### Retrieve your own credentials

You can retrieve credentials for a single Thread Border Router using [`retrieveCredentials(forBorderAgent:completion:)`](./thclient/retrievecredentials%28forborderagent,completion%29.md). To retrieve credentials for all of your Thread Border Routers, use [`retrieveAllCredentials(_:)`](./thclient/retrieveallcredentials%28_%29.md). If you only want to read the active Thread Border Router’s credentials, use [`retrieveAllActiveCredentials(_:)`](./thclient/retrieveallactivecredentials%28_%29.md). Retrieving records with these methods doesn’t require a person’s consent.

##### Update your Thread Border Router with preferred network credentials

If your Thread Border Router is already on the preferred network, use [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](./thclient/checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md) at app launch to determine if there are any modifications to the preferred network credentials. If there are, use [`retrievePreferredCredentials(_:)`](./thclient/retrievepreferredcredentials%28_%29.md) to read the updated preferred network credentials and store them to iCloud Keychain. This ensures that your Thread Border Router’s credentials always match the preferred network credentials.

##### Update the preferred network with Thread Border Router credentials

If your app detects a modification to the Thread credentials of a configured Border Router, update the credentials on iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](./thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md).

> ❗ **Important**: When you store your Thread Border Router credentials to iCloud Keychain using the Border Agent ID, that ID becomes a part of the preferred network. Any modifications that the Thread Border Router makes using that Border Agent ID also modifies the preferred network credentials in iCloud Keychain.

If you want to change your Thread Border Router credentials without affecting the preferred network credentials, delete the existing credentials in iCloud Keychain and then store the new credentials with a new Border Agent ID.

##### Detect a modified Service Set Identifier (SSID)

If a person changes the SSID of a Thread-capable Wi-Fi router, confirm that the credentials match the preferred network credentials with [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](./thclient/checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md). If not, read the preferred network credentials using [`retrievePreferredCredentials(_:)`](./thclient/retrievepreferredcredentials%28_%29.md) and store them in iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](./thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md).

## See Also

### Setting up Thread Border Routers
- [Getting started with ThreadNetwork](./getting-started-with-threadnetwork.md)
  Create a plan to build, test, and deploy your Thread Border Router app.
- [Configuring a Border Router](./configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/managing-thread-network-credentials)*