# canLoadObjects(ofClass:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func canLoadObjects<T>(ofClass: T.Type) -> Bool where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidragdropsession/canloadobjects(ofclass:)-6x43t)*