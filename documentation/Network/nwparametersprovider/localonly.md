# localOnly(_:)

**Framework**: Network  
**Kind**: method  
**Required**: Yes

Limit inbound connections to peers attached to the local link.

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
func localOnly(_ local: Bool) -> Self
```

#### Discussion

Listeners will only advertise services on the local link and will only accept connections from the local link.

## Parameters

- `local`: True if limited to local peers, false otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwparametersprovider/localonly(_:))*