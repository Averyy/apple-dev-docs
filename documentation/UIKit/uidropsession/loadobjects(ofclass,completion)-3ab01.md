# loadObjects(ofClass:completion:)

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
@preconcurrency func loadObjects<T>(ofClass: T.Type, completion: @escaping ([T]) -> Void) -> Progress where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropsession/loadobjects(ofclass:completion:)-3ab01)*