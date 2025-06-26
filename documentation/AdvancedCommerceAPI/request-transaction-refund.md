# Request Transaction Refund

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Request a refund for a one-time charge or subscription transaction.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)
- [Advanced Commerce API changelog](changelog.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)

#### Discussion

> **Note**: To use the `Request Transaction Refund` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the [`Cancel a Subscription`](cancel-a-subscription.md), [`Revoke Subscription`](revoke-subscription.md), and `Request Transaction Refund` APIs.

## Request Body

The request body.

## See Also

- [object RequestRefundRequest](requestrefundrequest.md)
  The request body for requesting a refund for a transaction.
- [object RequestRefundResponse](requestrefundresponse.md)
  The response body for a transaction refund request.
- [object RequestRefundItem](requestrefunditem.md)
  Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/request-transaction-refund)*