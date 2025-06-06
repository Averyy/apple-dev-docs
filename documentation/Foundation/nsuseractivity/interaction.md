# interaction

**Framework**: Foundation  
**Kind**: property

The SiriKit interaction object to use when configuring your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var interaction: INInteraction? { get }
```

#### Discussion

When SiriKit launches your app, it fills this property with the intent and response information that are the reason for launching your app. Use the information in this property to configure your app’s interface and show any relevant interaction details. If your app wasn’t launched because of a Siri interaction, the value in this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/interaction)*