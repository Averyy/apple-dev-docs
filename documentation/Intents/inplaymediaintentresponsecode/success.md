# INPlayMediaIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app is playing the media.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
case success
```

```c
INPlayMediaIntentResponseCodeSuccess
```

#### Discussion

Respond with this code after your app starts playing the media content in the [`application(_:handle:completionHandler:)`](../../UIKit/uiapplicationdelegate/application%28_,handle,completionhandler%29.md) method.

## See Also

### App
- [INPlayMediaIntentResponseCode.inProgress](./inprogress.md)
  The app is preparing to play the media content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaintentresponsecode/success)*