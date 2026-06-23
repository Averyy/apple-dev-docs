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

#### Discussion

When this device disconnects, any paired device that is still connected receives a notification to close its side of the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/close())*