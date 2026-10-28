# Networking and communication

**Framework**: Technology Overviews

Communicate with other devices over a network, extend the system’s core networking capabilities, and incorporate telephony into your apps.

Apps connect people to their friends and to the services they use in their daily lives. Many system frameworks use network-based services in their implementation, but you might also need to download files, communicate with RESTful endpoints, or support audio and video conversations over the network. When you do, the system frameworks provide the APIs you need to send and receive data over the network.

## Send and receive data and files across the network

When you want to send or receive data or files over the network, the [URL loading system](../Foundation/url-loading-system.md) provides the most robust option for making your requests. This system offers a straightforward API, which you use to:

- [Download](../Foundation/downloading-files-from-websites.md) files from a URL.
- [Download](../Foundation/fetching-website-data-into-memory.md) or [upload](../Foundation/uploading-data-to-a-website.md) data to a website or RESTful endpoint.
- [Upload a stream of data](../Foundation/uploading-streams-of-data.md) to a server.
- [Download files in the background](../Foundation/downloading-files-in-the-background.md) while your app is inactive.

The URL loading system uses a session-based approach to manage network requests. Each session’s configuration tells the system how to manage network requests and any changes that might occur. For example, you might [configure a session](../Foundation/urlsessionconfiguration.md) to download large files only over Wi-Fi instead of a cellular network. After creating the session, schedule tasks to send or receive the data you want. The system performs the tasks you schedule, using the session’s configuration data to manage authentication credentials, determine how to use caches and cookies, and select appropriate networks. To keep your app informed of progress, the session reports updates to a delegate object you provide.

Because the URL loading system is part of the [Foundation framework](../Foundation/Foundation.md), it’s available to all apps and is portable across different devices.

## Customize your app’s network-based communication

Modern networking requires many different communication protocols, and it’s important to know which ones to use for a given connection to a server. Technologies like the [URL loading system](../Foundation/url-loading-system.md) handle much of this complexity for you, providing a simple API to send and receive resources. However, there might be times when you need to manage a connection yourself to accommodate performance requirements or network behaviors. For example:

- You might want to minimize latency when sending game data to other devices.
- You might need multicast support for a streaming app, or want to prevent buffering during a live broadcast.
- You might want to handle transitions between different networks yourself in a mail or messaging app.

For more direct control over your app’s network requests, adopt the [Network](../Network/Network.md) framework. Use this framework to establish connections to servers and other devices using standard protocols like QUIC, TCP, UDP, or custom protocols you define. The framework offers ways to tune connections for your specific needs. It handles network-related changes gracefully, making it easy to track changes to network availability and move your connection to a more reliable network. It also supports the security and privacy options you need to protect the data you send.

To initiate a connection to another device, create an [NWConnection](../Network/nwconnection.md) object and configure it with the endpoint and parameters. The endpoint provides the address of the other device, but you can also specify Bonjour services and other values. When you start a connection, the system evaluates network conditions and selects the network that best meets your requirements. On the server side, a [NSListener](../Network/nwlistener.md) object responds to a connection request and sends responses from your server back to the client.

## Extend the core networking capabilities of a device

If your app has custom networking requirements, you can augment the core network’s capabilities in many ways. For example:

- Create custom [Wi-Fi configurations](../NetworkExtension/wi-fi-configuration.md).
- Implement a helper to [authenticate hotspot networks](../NetworkExtension/hotspot-helper.md).
- Create and manage [virtual private network (VPN)](../NetworkExtension/NetworkExtension.md) configurations, or implement your own.
- Create a [network relay configuration](../NetworkExtension/relays.md).
- Implement on-device [network content](../NetworkExtension/NetworkExtension.md) or [URL](../NetworkExtension/url-filters.md) filters.
- Create and manage system-wide [DNS configurations](../NetworkExtension/NetworkExtension.md).
- Create your own [push notification server](../NetworkExtension/local-push-connectivity.md) on a local network.

Implement the capabilities you need using the types of the [Network Extension](../NetworkExtension/NetworkExtension.md) framework. Most features require you to put your code in an app extension, which you deliver to customers inside an app. Not all features are available on all platforms, so check the documentation to make sure the feature you want is available.

## Advertise a device using Bonjour

Bonjour is Apple’s implementation of *zero-configuration networking*, a process that simplifies device setup and interactions on a local network. With Bonjour, apps can browse for devices on the network without knowing specific network addresses. Bonjour provides a list of available devices that support the requested capability. For example, the system printing panel looks for printers on the local network and presents them as relevant targets for a print job.

To make your app’s custom capabilities available on the network, use the [Network](../Network/Network.md) framework to advertise them using Bonjour. Specifically, configure a [listener](../Network/nwlistener.md) to handle incoming requests from other devices. To place a request to your capability, clients configure an [NWConnection](../Network/nwconnection.md) object with the specific [endpoint](../Network/nwendpoint.md) you advertise using Bonjour.

## Add dialing and conversation features to your app

If your app manages its own Voice-over-IP (VoIP) services, [LiveCommunicationKit](../LiveCommunicationKit/LiveCommunicationKit.md) supports your app’s conversation infrastructure. Use that framework to notify the system of your app’s status, which the system uses to handle inbound calls. For example, if someone is on a call when a new call comes in, the system might ask the person if they want to hang up the current call and accept the new one. If your app manages calls, but doesn’t provide its own VoIP services, manage conversations using [LiveCommunicationKit](../LiveCommunicationKit/LiveCommunicationKit.md), which routes conversations to the appropriate app.

In some regions, the owner of a device designates one app to handle incoming and outgoing conversations. When multiple apps are present, the system needs to know which one to use for incoming conversations. On iPhone, the Phone app is typically the default calling and dialer app, but people can choose different apps. If you’re building a conversation app, adopt the [LiveCommunicationKit](../LiveCommunicationKit/LiveCommunicationKit.md) framework to prepare your app to become the [default dialer](../LiveCommunicationKit/preparing-your-app-to-be-the-default-dialer-app.md) and [default calling](../CallKit/preparing-your-app-to-be-the-default-calling-app.md) app. In addition to handling calls, the default dialer app has access to the conversation history on the person’s device, as well as other benefits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/networking-and-communication)*