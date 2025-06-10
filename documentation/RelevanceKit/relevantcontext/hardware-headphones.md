# hardware(headphones:)

**Framework**: RelevanceKit  
**Kind**: method

Tells the system a widget is relevant when a person’s headphones are connected.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func hardware(headphones: RelevantContext.HeadphonesCondition) -> RelevantContext
```

#### Return Value

A contextual clue that the system uses to determine the relevance of a widget in the Smart Stack on Apple Watch.

#### Discussion

Setting a [`RelevantContext.HeadphonesCondition`](relevantcontext/headphonescondition.md) to signal relevance to the system doesn’t give you access to fitness activity and information. If contextual fitness information isn’t available to the system, fitness clues to signal relevance don’t have an effect.

> **Note**: Smart Stacks are available in iOS, iPadOS, and watchOS. However, functionality provided by RelevanceKit API is only available in watchOS. Calling its API on other platforms doesn’t have any effect. For more information, refer to [`Increasing the visibility of widgets in Smart Stacks`](https://developer.apple.com/documentation/WidgetKit/Widget-Suggestions-In-Smart-Stacks).

## Parameters

- `headphones`: A value that indicates connected headphones.

## See Also

- [RelevantContext.HeadphonesCondition](relevantcontext/headphonescondition.md)
  A structure that indicates whether a person’s headphones are connected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/relevancekit/relevantcontext/hardware(headphones:))*