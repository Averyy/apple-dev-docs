# wifiAware(_:active:)

**Framework**: Network  
**Kind**: method

Sets a `NetworkListener` to publish Wi-Fi Aware services to the selected paired devices.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
static func wifiAware(_ action: WAPublisherListener.Action, active requestedDuration: Duration? = nil) -> Self
```

#### Return Value

A new `ListenerProvider` containing the `.wifiAware()` instruction that will configure a `NetworkListener` as a Wi-Fi Aware publisher.

#### Discussion

The code snippet below is an example of how to set the `NetworkListener`.

```swift
NetworkListener(for: .wifiAware(.connecting(to:service, from:.selected(devices))) )
```

## Parameters

- `action`: The specific Wi-Fi Aware operation to perform, and the service & devices to perform it on.
- `requestedDuration`: Optional duration requested to keep the   publishing. The default value of   instructs the system to stay active for long enough to guarantee the action completes with all nearby target devices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/listenerprovider/wifiaware(_:active:))*