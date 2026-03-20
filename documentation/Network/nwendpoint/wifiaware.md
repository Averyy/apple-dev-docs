# wifiAware

**Framework**: Network  
**Kind**: property

Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var wifiAware: WAEndpoint? { get }
```

#### Return Value

A new endpoint that can be used to connect over Wi-Fi Aware, or `nil` if it not compatible with Wi-Fi Aware.

#### Discussion

The returned endpoint can be used to connect to a remote `NetworkListener` that accepts additional Wi-Fi Aware connections without publishing a service, via  `WiFiAware/WAPublisherListener/Action/addingConnections(from:)`

The returned endpoint will use Wi-Fi Aware as a transport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwendpoint/wifiaware)*