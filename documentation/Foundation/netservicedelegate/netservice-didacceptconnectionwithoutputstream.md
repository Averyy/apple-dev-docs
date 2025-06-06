# netService(_:didAcceptConnectionWith:outputStream:)

**Framework**: Foundation  
**Kind**: method

Called when a client connects to a service managed by Bonjour.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func netService(_ sender: NetService, didAcceptConnectionWith inputStream: InputStream, outputStream: OutputStream)
```

#### Discussion

When you publish a service, if you set the [`listenForConnections`](netservice/options/listenforconnections.md) flag in the service options, the service object accepts connections on behalf of your app. Later, when a client connects to that service, the service object calls this method to provide the app with a pair of streams for communicating with that client.

## Parameters

- `sender`: The net service object that the client connected to.
- `inputStream`: A stream object for receiving data from the client.
- `outputStream`: A stream object for sending data to the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/netservicedelegate/netservice(_:didacceptconnectionwith:outputstream:))*