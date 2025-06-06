# result(opensIntent:dialog:view:)

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
static func result<OpensAppIntent, Content>(opensIntent: OpensAppIntent, dialog: IntentDialog, view: Content = EmptyView()) -> Self where Self == IntentResultContainer<Never, OpensAppIntent, _SnippetViewContainer, IntentDialog>, OpensAppIntent : AppIntent, Content : View
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentresult/result(opensintent:dialog:view:)-8wkpg)*