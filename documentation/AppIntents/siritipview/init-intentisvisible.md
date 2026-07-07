# init(intent:isVisible:)

**Framework**: App Intents  
**Kind**: init

Creates a `SiriTipView` for the associated action that displays when the binding to a Boolean value is true .

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<Intent>(intent: Intent, isVisible: Binding<Bool>? = nil) where Intent : AppIntent
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/init(intent:isvisible:))*