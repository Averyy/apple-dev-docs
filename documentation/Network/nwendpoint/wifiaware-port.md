# wifiAware(port:)

**Framework**: Network  
**Kind**: method

Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware on the specified port, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func wifiAware(port: NWEndpoint.Port) -> WAEndpoint?
```

#### Return Value

A new endpoint that can be used to connect over Wi-Fi Aware, or `nil` if it not compatible with Wi-Fi Aware.

#### Discussion

The returned endpoint can be used to connect to a remote `NetworkListener` that accepts additional Wi-Fi Aware connections without publishing a service, via  `WiFiAware/WAPublisherListener/Action/addingConnections(from:)`

The returned endpoint will use Wi-Fi Aware as a transport.

## Parameters

- `port`: The port to use for this endpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/wifiaware(port:))*