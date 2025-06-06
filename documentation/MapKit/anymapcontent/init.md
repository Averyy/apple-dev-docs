# init(_:)

**Framework**: MapKit  
**Kind**: init

Create an instance that type-erases `base`.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst ?+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
@MainActor
@preconcurrency init<Content>(_ base: Content) where Content : MapContent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/anymapcontent/init(_:))*