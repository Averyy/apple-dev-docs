# close()

**Framework**: ProximityReader  
**Kind**: method

Closes the engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func close() async throws
```

## Mentions

- [Adding support for Tap to Share to your app](adding-support-for-tap-to-share-to-your-app.md)

#### Discussion

When this device disconnects, any paired device that is still connected receives a notification to close its side of the session.

## See Also

- [CustomerEngagementSession.Configuration](customerengagementsession/configuration-swift.struct.md)
  A set of configuration options for a customer engagement session.
- [let configuration: CustomerEngagementSession.Configuration](customerengagementsession/configuration-swift.property.md)
  Configuration for this session.
- [func open(using: CustomerEngagement.Token?) async throws](customerengagementsession/open(using:).md)
  Opens the engagement session.
- [CustomerEngagementSession.Token](customerengagementsession/token-swift.struct.md)
  A session token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/close())*