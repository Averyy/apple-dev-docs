# ThreadNetwork

**Framework**: ThreadNetwork  
**Kind**: module

Share credentials and choose a designated network for each home.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 16.1+
- macOS 13.0+
- visionOS 1.0+

#### Overview

[`Thread`](https://developer.apple.comhttps://www.threadgroup.org) is a low-power wireless mesh networking protocol based on the universally supported Internet Protocol (IP). It’s built using open and proven standards. Thread networks have no single point of failure and include the ability to maintain communication when other devices go offline. For example, if you remove a Border Router, nearby Thread devices can still communicate with their neighbors.

![A cross-cut section of a two-story house. The living room on the bottom floor shows a fan, a HomePod mini, a light bulb, and a remote, all connected wirelessly with Thread. The upstairs rooms have a ceiling fan, a HomePod, several light bulbs, and a wall plug connected wirelessly with Thread. The kitchen on the first floor has an oven and a light bulb connected wirelessly to Thread. The front yard has a landscape light under a tree connected wireless to Thread.](https://docs-assets.developer.apple.com/published/7c8ccd1019a7919ab4ed39e7ee04d814/threadnetwork-1%402x.png)

The ThreadNetwork framework helps clients share credentials in a safe and secure manner, and automatically chooses a network for each home, known as the .

The Border Router hardware device is a key element of Thread networks. It routes IP traffic between Thread and Wi-Fi or Ethernet networks, and enables iOS devices to communicate with Thread devices. HomePod and HomePod mini are examples of Border Routers.

The robustness of Thread relies on member devices forwarding packets to their neighbors on the network. This creates a mesh that strengthens the network and increases reliability. For example, adding an additional Border Router to a Thread network improves coverage.

![A Thread Border Router connects wirelessly to two end devices. One is an end device icon that represents a light switch. The other is a sleepy end device icon that represents a wireless, battery-powered sensor.](https://docs-assets.developer.apple.com/published/1c35203952259f42eb47e0efb735ae20/threadnetwork-2%402x.png)

 are Thread devices located at the endpoint of a Thread network. They communicate with other Thread devices, but don’t forward packets on their behalf.  are end devices that run in low-power mode because they’re usually battery-powered. An example of a sleepy end device is a temperature sensor that runs on a battery. The  manages routers on a Thread network. There can only be one Thread Leader on the network at any time.

To learn more about Thread, visit the [`OpenThread Guides`](https://developer.apple.comhttps://openthread.io/guides) and [`What is Thread?`](https://developer.apple.comhttps://openthread.io/guides/thread-primer).

## Topics

### Setting up Border Routers
- [Configuring a Border Router](configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.
- [Managing Thread network credentials](managing-thread-network-credentials.md)
  Store, delete, retrieve, and update Thread network credentials on your Apple device.
### Managing clients and sharing credentials
- [com.apple.developer.networking.manage-thread-network-credentials](../BundleResources/Entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [class THClient](thclient.md)
  A class that supports safely sharing Thread credentials between multiple clients.
- [class THCredentials](thcredentials.md)
  A class that contains credentials for a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ThreadNetwork)*