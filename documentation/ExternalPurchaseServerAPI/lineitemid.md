# lineItemId

**Framework**: External Purchase Server API  
**Kind**: typealias

A unique identifier for the line item, that you determine.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string lineItemId
```

## Mentions

- [Reporting corrections](reportcorrections.md)

#### Discussion

Maximum length: 128

The [`lineItemId`](lineitemid.md) string must be unique for each app. Using UUIDs is recommended. All line item objects have a [`lineItemId`](lineitemid.md), including:

- [`OneTimeBuyLineItem`](onetimebuylineitem.md)
- [`RefundLineItem`](refundlineitem.md)
- [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/lineitemid)*