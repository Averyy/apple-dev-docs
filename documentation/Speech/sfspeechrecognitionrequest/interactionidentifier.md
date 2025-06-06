# interactionIdentifier

**Framework**: Speech  
**Kind**: property

An identifier string that you use to describe the type of interaction associated with the speech recognition request.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var interactionIdentifier: String? { get set }
```

#### Discussion

If different parts of your app have different speech recognition needs, you can use this property to identify the part of your app that is making each request. For example, if one part of your app lets users speak phone numbers and another part lets users speak street addresses, consistently identifying the part of the app that makes a recognition request may help improve the accuracy of the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfspeechrecognitionrequest/interactionidentifier)*