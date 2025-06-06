# MusicAuthorization.Status.restricted

**Framework**: MusicKit  
**Kind**: case

Apps on this device can’t access MusicKit in a way that the user can’t change.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
case restricted
```

#### Discussion

In this scenario, don’t prompt for authorization.

An example of this situation is when the device is in education mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicauthorization/status/restricted)*