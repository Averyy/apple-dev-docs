# SubscriptionOptionGroupStyle

**Framework**: StoreKit  
**Kind**: protocol

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol SubscriptionOptionGroupStyle
```

## Topics

### Getting built-in subscription option group styles
- [static var automatic: AutomaticSubscriptionOptionGroupStyle](subscriptionoptiongroupstyle/automatic.md)
- [static var links: LinksSubscriptionOptionGroupStyle](subscriptionoptiongroupstyle/links.md)
- [static var tabs: TabsSubscriptionOptionGroupStyle](subscriptionoptiongroupstyle/tabs.md)
### Supporting types
- [struct AutomaticSubscriptionOptionGroupStyle](automaticsubscriptionoptiongroupstyle.md)
- [struct LinksSubscriptionOptionGroupStyle](linkssubscriptionoptiongroupstyle.md)
- [struct TabsSubscriptionOptionGroupStyle](tabssubscriptionoptiongroupstyle.md)
- [struct SubscriptionOptionGroupStyleOutput](subscriptionoptiongroupstyleoutput.md)

## Relationships

### Conforming Types
- [AutomaticSubscriptionOptionGroupStyle](automaticsubscriptionoptiongroupstyle.md)
- [LinksSubscriptionOptionGroupStyle](linkssubscriptionoptiongroupstyle.md)
- [TabsSubscriptionOptionGroupStyle](tabssubscriptionoptiongroupstyle.md)

## See Also

- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View](../SwiftUI/View/subscriptionStoreOptionGroupStyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](storecontent/subscriptionstoreoptiongroupstyle(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptiongroupstyle)*