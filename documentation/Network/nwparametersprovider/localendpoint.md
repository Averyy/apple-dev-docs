# localEndpoint(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Specify a specific endpoint to use as the local endpoint.

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
func localEndpoint(_ endpoint: NWEndpoint?) -> Self
```

#### Discussion

For connections, this will be used to initiate traffic; for listeners, this will be used for receiving incoming connections.

## Parameters

- `endpoint`: The local endpoint to require, or   if none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/localendpoint(_:))*