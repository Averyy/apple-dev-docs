# Networking and communication

**Framework**: Technology Overviews

Communicate with other devices over a network, extend the system’s core networking capabilities, and incorporate telephony into your apps.

Apps connect people to their friends and to the services they use in their daily lives. Many system frameworks use network-based services in their implementation, but you might also need to download files, communicate with RESTful endpoints, or support audio and video conversations over the network. When you do, the system frameworks provide the APIs you need to send and receive data over the network.

#### Send and Receive Data and Files Across the Network

When you want to send or receive data or files over the network, the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system) provides the most robust option for making your requests. This system offers a straightforward API, which you use to:

- [`Downloading files from websites`](https://developer.apple.com/documentation/Foundation/downloading-files-from-websites) files from a URL.
- [`Fetching website data into memory`](https://developer.apple.com/documentation/Foundation/fetching-website-data-into-memory) or [`Uploading data to a website`](https://developer.apple.com/documentation/Foundation/uploading-data-to-a-website) data to a website or RESTful endpoint.
- [`Uploading streams of data`](https://developer.apple.com/documentation/Foundation/uploading-streams-of-data) to a server.
- [`Downloading files in the background`](https://developer.apple.com/documentation/Foundation/downloading-files-in-the-background) while your app is inactive.

The URL loading system uses a session-based approach to manage network requests. Each session’s configuration tells the system how to manage network requests and any changes that might occur. For example, you might [`URLSessionConfiguration`](https://developer.apple.com/documentation/Foundation/URLSessionConfiguration) to download large files only over Wi-Fi instead of a cellular network. After creating the session, schedule tasks to send or receive the data you want. The system performs the tasks you schedule, using the session’s configuration data to manage authentication credentials, determine how to use caches and cookies, and select appropriate networks. To keep your app informed of progress, the session reports updates to a delegate object you provide.

Because the URL loading system is part of the [`Foundation`](https://developer.apple.com/documentation/Foundation), it’s available to all apps and is portable across different devices.

#### Customize Your Apps Network Based Communication

Modern networking requires many different communication protocols, and it’s important to know which ones to use for a given connection to a server. Technologies like the [`URL Loading System`](https://developer.apple.com/documentation/Foundation/url-loading-system) handle much of this complexity for you, providing a simple API to send and receive resources. However, there might be times when you need to manage a connection yourself to accommodate performance requirements or network behaviors. For example:

- You might want to minimize latency when sending game data to other devices.
- You might need multicast support for a streaming app, or want to prevent buffering during a live broadcast.
- You might want to handle transitions between different networks yourself in a mail or messaging app.

For more direct control over your app’s network requests, adopt the [`Network`](https://developer.apple.com/documentation/Network) framework. Use this framework to establish connections to servers and other devices using standard protocols like QUIC, TCP, UDP, or custom protocols you define. The framework offers ways to tune connections for your specific needs. It handles network-related changes gracefully, making it easy to track changes to network availability and move your connection to a more reliable network. It also supports the security and privacy options you need to protect the data you send.

To initiate a connection to another device, create an [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection) object and configure it with the endpoint and parameters. The endpoint provides the address of the other device, but you can also specify Bonjour services and other values. When you start a connection, the system evaluates network conditions and selects the network that best meets your requirements. On the server side, a [`NWListener`](https://developer.apple.com/documentation/Network/NWListener) object responds to a connection request and sends responses from your server back to the client.

#### Extend the Core Networking Capabilities of a Device

If your app has custom networking requirements, you can augment the core network’s capabilities in many ways. For example:

- Create custom [`Wi-Fi configuration`](https://developer.apple.com/documentation/NetworkExtension/wi-fi-configuration).
- Implement a helper to [`Hotspot helper`](https://developer.apple.com/documentation/NetworkExtension/hotspot-helper).
- Create and manage [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension#Virtual-private-networks) configurations, or implement your own.
- Create a [`Relays`](https://developer.apple.com/documentation/NetworkExtension/relays).
- Implement on-device [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension#Content-filters) or [`URL filters`](https://developer.apple.com/documentation/NetworkExtension/url-filters) filters.
- Create and manage system-wide [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension#DNS-configurations).
- Create your own [`Local push connectivity`](https://developer.apple.com/documentation/NetworkExtension/local-push-connectivity) on a local network.

Implement the capabilities you need using the types of the [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) framework. Most features require you to put your code in an app extension, which you deliver to customers inside an app. Not all features are available on all platforms, so check the documentation to make sure the feature you want is available.

#### Advertise a Device Using Bonjour

Bonjour is Apple’s implementation of , a process that simplifies device setup and interactions on a local network. With Bonjour, apps can browse for devices on the network without knowing specific network addresses. Bonjour provides a list of available devices that support the requested capability. For example, the system printing panel looks for printers on the local network and presents them as relevant targets for a print job.

To make your app’s custom capabilities available on the network, use the [`Network`](https://developer.apple.com/documentation/Network) framework to advertise them using Bonjour. Specifically, configure a [`NWListener`](https://developer.apple.com/documentation/Network/NWListener) to handle incoming requests from other devices. To place a request to your capability, clients configure an [`NWConnection`](https://developer.apple.com/documentation/Network/NWConnection) object with the specific [`NWEndpoint`](https://developer.apple.com/documentation/Network/NWEndpoint) you advertise using Bonjour.

#### Add Dialing and Conversation Features to Your App

If your app manages its own Voice-over-IP (VoIP) services, [`LiveCommunicationKit`](https://developer.apple.com/documentation/LiveCommunicationKit) supports your app’s conversation infrastructure. Use that framework to notify the system of your app’s status, which the system uses to handle inbound calls. For example, if someone is on a call when a new call comes in, the system might ask the person if they want to hang up the current call and accept the new one. If your app manages calls, but doesn’t provide its own VoIP services, manage conversations using [`LiveCommunicationKit`](https://developer.apple.com/documentation/LiveCommunicationKit), which routes conversations to the appropriate app.

In some regions, the owner of a device designates one app to handle incoming and outgoing conversations. When multiple apps are present, the system needs to know which one to use for incoming conversations. On iPhone, the Phone app is typically the default calling and dialer app, but people can choose different apps. If you’re building a conversation app, adopt the [`LiveCommunicationKit`](https://developer.apple.com/documentation/LiveCommunicationKit) framework to prepare your app to become the [`Preparing your app to be the default dialer app`](https://developer.apple.com/documentation/LiveCommunicationKit/preparing-your-app-to-be-the-default-dialer-app) and [`Preparing your app to be the default calling app`](https://developer.apple.com/documentation/CallKit/Preparing-your-app-to-be-the-default-calling-app) app. In addition to handling calls, the default dialer app has access to the conversation history on the person’s device, as well as other benefits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/networking-and-communication)*