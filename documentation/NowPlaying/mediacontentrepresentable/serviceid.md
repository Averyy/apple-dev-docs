# serviceID

**Framework**: Now Playing  
**Kind**: property  
**Required**: Yes

A unique identifier for the service provider this content belongs to.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var serviceID: String? { get set }
```

#### Discussion

If the content belongs to a channel or subscription service, the system uses this identifier to coordinate various types of Now Playing content from that particular service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediacontentrepresentable/serviceid)*