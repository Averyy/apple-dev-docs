# Configuring a Border Router

**Framework**: ThreadNetwork  
**Role**: Article

Set up or add a Border Router on a Thread network.

#### Overview

The Border Router acts as a bridge between the Thread and Wi-Fi or Ethernet networks in a home. Multiple Border Routers on the preferred network strengthen communication between devices and improve the network’s resiliency.

##### Set up a new Border Router on the preferred network

To begin setup, first check for a configured preferred network using [`isPreferredNetworkAvailable(completion:)`](./thclient/ispreferrednetworkavailable%28completion%29.md). If one is already configured, use [`retrievePreferredCredentials(_:)`](./thclient/retrievepreferredcredentials%28_%29.md) to read the credentials.

> **Note**: Retrieving preferred network credentials requires user consent.

If a preferred network isn’t available, you must create a new Thread network and configure the Thread Border Router with this information.

After you configure the Border Router, store the credentials to iCloud Keychain using [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](./thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md).

> ❗ **Important**: If you’re setting up a Thread-capable Wi-Fi router, read the preferred network only after the user configures the Wi-Fi SSID on that router.

Storing credentials marks the newly created Thread network as the preferred network in iCloud Keychain. This process makes the Thread network immediately available for devices to join.

##### Add a Border Router to the preferred network

If you’re setting up another Thread Border Router on the preferred network, ensure that the previously cached preferred network credentials match using [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](./thclient/checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md). If they don’t match, re-read the preferred network credentials from iCloud Keychain using
[`retrievePreferredCredentials(_:)`](./thclient/retrievepreferredcredentials%28_%29.md) and configure the Border Router with those credentials.

After you’ve configured the Border Router, use [`storeCredentials(forBorderAgent:activeOperationalDataSet:completion:)`](./thclient/storecredentials%28forborderagent,activeoperationaldataset,completion%29.md) to store the Border Router’s Thread network credentials to iCloud Keychain. You can set up any number of Border Routers this way.

> ❗ **Important**: Use [`isPreferredNetworkAvailable(completion:)`](./thclient/ispreferrednetworkavailable%28completion%29.md) before calling  [`checkPreferredNetwork(forActiveOperationalDataset:completion:)`](./thclient/checkpreferrednetwork%28foractiveoperationaldataset,completion%29.md) to avoid a scenario in which a user configures an initial device at one home, and a subsequent device at a different home.

## See Also

### Setting up Thread Border Routers
- [Getting started with ThreadNetwork](./getting-started-with-threadnetwork.md)
  Create a plan to build, test, and deploy your Thread Border Router app.
- [Managing Thread network credentials](./managing-thread-network-credentials.md)
  Store, retrieve, update, and delete Thread network credentials on your Apple device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/threadnetwork/configuring-a-border-router)*