# systemContext

**Framework**: App Intents  
**Kind**: property

Context information that’s available while the system performs the app intent’s action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var systemContext: IntentSystemContext { get }
```

#### Discussion

Access information the system provides to your app intent while it performs its action in its [`perform()`](appintent/perform().md) implementation. The provided information can vary and include information for each platform. For example, in watchOS, the intent system context includes a precise timestamp when a person started the app intent’s action using the Action button on Apple Watch Ultra.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/emptysnippetintent/systemcontext)*