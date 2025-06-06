# userEngaged(_:visibleItems:interaction:)

**Framework**: Core Spotlight  
**Kind**: method

Notifies the system that someone engaged with a specific search result in your app’s interface.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func userEngaged(_ item: CSUserQuery.Item, visibleItems: [CSUserQuery.Item], interaction: CSUserQuery.UserInteractionKind)
```

#### Discussion

When someone selects or interacts with a specific search result in your app’s UI, call this method to tell Spotlight about the interaction. Reporting this type of engagement helps Spotlight deliver better results more quickly in future queries. It also improves the ranked results Spotlight delivers to your app. The system keeps all information about these interactions on the current device

## Parameters

- `item`: The search result that someone chose.
- `visibleItems`: The set of search results your app was displaying.

## See Also

- [func userEngaged(CSUserQuery.Suggestion, visibleSuggestions: [CSUserQuery.Suggestion], interaction: CSUserQuery.UserInteractionKind)](csuserquery/userengaged(_:visiblesuggestions:interaction:).md)
  Notifies the system that someone engaged with a specific text completion in your app’s interface.
- [CSUserQuery.UserInteractionKind](csuserquery/userinteractionkind.md)
  Constants that indicate how someone engaged with search-related content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/userengaged(_:visibleitems:interaction:))*