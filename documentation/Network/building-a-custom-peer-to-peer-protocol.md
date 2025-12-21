# Building a custom peer-to-peer protocol

**Framework**: Network

Use networking frameworks to create a custom protocol for playing a game across iOS, iPadOS, watchOS, and tvOS devices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- watchOS 9.0+
- Xcode 15.0+

#### Overview

This TicTacToe sample code project creates a networked game that you can play between different devices, communicating with a custom protocol. The game offers two ways to play:

- On Apple TV, the game uses [`DeviceDiscoveryUI`](https://developer.apple.com/documentation/DeviceDiscoveryUI) to discover nearby iOS, iPadOS, and watchOS devices. After connecting, you can use your device to play against an AI opponent on Apple TV.
- On iOS and iPadOS devices, the game uses Bonjour and TLS to establish secure connections between nearby devices. You can use this mode to play a peer-to-peer two-player game.

> **Note**: This sample code project is associated with WWDC22 session [`110339: Build device-to-device interactions with the Network framework`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110339/). It’s also associated with WWDC 2020 session [`10110: Support local network privacy in your app`](https://developer.apple.comhttps://developer.apple.com/wwdc20/10110/) and with WWDC 2019 session [`713: Advances in Networking, Part 2`](https://developer.apple.comhttps://developer.apple.com/wwdc19/713/).

## See Also

- [Connecting iPadOS and visionOS apps over the local network](../visionOS/connecting-ipados-and-visionos-apps-over-the-local-network.md)
  Build an iPadOS companion app to control your visionOS app.
- [class NWProtocolTCP](nwprotocoltcp.md)
  A network protocol for connections that use the Transmission Control Protocol.
- [class NWProtocolTLS](nwprotocoltls.md)
  A network protocol for connections that use Transport Layer Security.
- [class NWProtocolQUIC](nwprotocolquic.md)
  A network protocol for connections that use the QUIC transport protocol.
- [class NWProtocolUDP](nwprotocoludp.md)
  A network protocol for connections that use the User Datagram Protocol.
- [class NWProtocolIP](nwprotocolip.md)
  A network protocol for configuring the Internet Protocol on connections.
- [class NWProtocolWebSocket](nwprotocolwebsocket.md)
  A network protocol for connections that use WebSocket.
- [class NWProtocolFramer](nwprotocolframer.md)
  A customizable network protocol for defining application message parsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/building-a-custom-peer-to-peer-protocol)*