# localPort(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Specify a specific port to use as the local endpoint, letting the system select the address.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
func localPort(_ port: NWEndpoint.Port) -> Self
```

#### Discussion

For connections, this will be used to initiate traffic; for listeners, this will be used for receiving incoming connections.

## Parameters

- `port`: The local port to require.   Force a specific local port to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/localport(_:))*