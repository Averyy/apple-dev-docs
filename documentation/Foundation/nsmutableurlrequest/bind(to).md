# bind(to:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Binds a URL request to the network interface associated with the hotspot helper command instance.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func bind(to command: NEHotspotHelperCommand)
```

```objc
- (void) bindToHotspotHelperCommand:(NEHotspotHelperCommand *) command;
```

#### Discussion

Apps that participate in joining Wi-Fi hotspot networks use the APIs in the [Network Extension](../../NetworkExtension/NetworkExtension.md) framework to authenticate with hotspots. Ordinarily, [`URLSession`](../urlsession.md) will use the default interface, which may be WWAN. By binding to a hotspot helper command, you force a request to use Wi-Fi to communicate with the hotspot.

## Parameters

- `command`: The hotspot helper command to bind the request to.

## See Also

### Related Documentation
- [Network Extension](../../NetworkExtension/NetworkExtension.md)
  Customize and extend core networking features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmutableurlrequest/bind(to:))*