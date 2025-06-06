# result(value:opensIntent:content:)

**Framework**: App Intents  
**Kind**: method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func result<Value, OpensAppIntent, Content>(value: Value, opensIntent: OpensAppIntent, @ViewBuilder content: () -> Content) -> Self where Self == IntentResultContainer<Value, OpensAppIntent, _SnippetViewContainer, Never>, Value : _IntentValue, OpensAppIntent : AppIntent, Content : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(value:opensintent:content:)-95tmb)*