# relevanceProviders

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Additional relevance information attached to the shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var relevanceProviders: [INRelevanceProvider] { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy) NSArray<INRelevanceProvider *> * relevanceProviders;
```

*macOS*

```objc
@property (atomic, copy) NSArray<INRelevanceProvider *> * relevanceProviders;
```

## Mentions

- [Defining Relevant Shortcuts for the Siri Watch Face](../../SiriKit/defining-relevant-shortcuts-for-the-siri-watch-face.md)

#### Discussion

To attach relevance information to the shortcut, like a daily routine or location, set this property to an array of [`INRelevanceProvider`](../inrelevanceprovider.md) objects. The system uses this relevance information to suggest widgets on a Smart Stack, or offer shortcuts on the Siri watch face. If you provide an empty array, the system relies on other relevance cues like user interactions to determine what widget to suggest or shortcut to offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrelevantshortcut/relevanceproviders)*