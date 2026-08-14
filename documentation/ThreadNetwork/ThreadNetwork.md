# ThreadNetwork

**Framework**: ThreadNetwork  
**Kind**: module

Create robust, smart device networks using Thread Border Routers.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS 1.0+

#### Overview

The [`Thread`](https://developer.apple.comhttps://www.threadgroup.org) standard is a low-power, wireless mesh networking protocol that runs over standard Internet protocols that allows smart home devices — such as Apple Home—compatible devices — to communicate with each other. Mesh networks are peer-to-peer networks that don’t have a single, centrally defined router, eliminating the risk of a single point of failure. They can dynamically reconfigure themselves and discover nearby peer devices with shared credentials. This allows them to maintain communication even when some devices go offline, like the following image illustrates:

![A cross-cut section of a two-story house. The living room on the bottom floor shows a fan, a HomePod mini, a light bulb, and a remote, all connected wirelessly with Thread. The upstairs rooms have a ceiling fan, a HomePod, several light bulbs, and a wall plug connected wirelessly with Thread. The kitchen on the first floor has an oven and a light bulb connected wirelessly to Thread. The front yard has a landscape light under a tree connected wireless to Thread.](/images/com.apple.ThreadNetwork/threadnetwork-1@2x.png)

The robustness of Thread relies on member devices forwarding packets to their neighbors; this creates a mesh that strengthens and increases its reliability as people add more devices. The mesh can also provide faster communication, especially over large networks, because there are more paths for messages to take across the network.

The Thread Border Router hardware device is a key element of Thread networks. It routes IP traffic between Thread and Wi-Fi or Ethernet networks, and enables iOS devices to communicate with Thread devices. HomePod and HomePod mini are examples of Border Routers.

To create your own Thread Border Router, use the ThreadNetwork framework to configure and manage your router. The ThreadNetwork framework helps you choose the right Thread network for your certified Thread Border Router.

#### Learn About Thread Network Device Roles

A Thread network can contain several types of devices that someone can deploy in many combinations:

- **Thread Border Router**: A device that provides a connection between the Thread network and an existing WiFi or Ethernet network. These devices may be standalone, acting solely as routers, or they may support additional functionality. For example, HomePod (second Generation), HomePod Mini, and AppleTV 4K are all examples of Thread Border Routers.
- **Thread Leader**: A device that manages routers on a Thread network. A Thread network can only have one Thread Leader at any time; member devices select a Thread Leader based on various routing characteristics of the network in order to optimize performance.
- **End device**: Thread devices located at the endpoints of a Thread network. They can communicate directly with other Thread devices, but don’t operate as routers forwarding packets on their behalf.
- **Sleepy End device**: End devices that run in low-power mode and are often battery powered. To conserve power they generally only wake up occasionally (which is why they’re referred to as “sleepy”) to report whatever data the device collects. Examples of sleepy devices include battery-powered temperature sensors or air quality monitors.

The following image illustrates the connections between a Border Router, an end device, and a sleepy end device:

![A Thread Border Router connects wirelessly to two end devices. One is an end device icon that represents a light switch. The other is a sleepy end device icon that represents a wireless, battery-powered sensor.](/images/com.apple.ThreadNetwork/threadnetwork-2@2x.png)

To learn more about Thread, visit the [`OpenThread Guides`](https://developer.apple.comhttps://openthread.io/guides) and [`What is Thread?`](https://developer.apple.comhttps://www.threadgroup.org/What-is-Thread/Overview)

> **Note**: Thread standard is developed by the Thread Group, and that use of “Thread” to describe Border Routers is subject to Thread Group’s Trademark and Certification Policies.

To learn more about the process of ThreadNetwork development, see [`Getting started with ThreadNetwork`](getting-started-with-threadnetwork.md).

## Topics

### Setting up Thread Border Routers
- [Getting started with ThreadNetwork](getting-started-with-threadnetwork.md)
  Create a plan to build, test, and deploy your Thread Border Router app.
- [Configuring a Border Router](configuring-a-border-router.md)
  Set up or add a Border Router on a Thread network.
- [Managing Thread network credentials](managing-thread-network-credentials.md)
  Store, retrieve, update, and delete Thread network credentials on your Apple device.
### Managing clients and sharing credentials
- [com.apple.developer.networking.manage-thread-network-credentials](../bundleresources/entitlements/com.apple.developer.networking.manage-thread-network-credentials.md)
  A Boolean value that indicates whether the app can use ThreadNetwork.
- [class THClient](thclient.md)
  A class that supports safely sharing Thread credentials between multiple clients.
- [class THCredentials](thcredentials.md)
  A class that contains credentials for a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ThreadNetwork)*