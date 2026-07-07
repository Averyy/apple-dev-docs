# open(using:)

**Framework**: ProximityReader  
**Kind**: method

Opens the engagement session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func open(using token: CustomerEngagement.Token? = nil) async throws
```

#### Discussion

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the open request fails. This method can also throw `Foundation/URLError`.

## Parameters

- `token`: `The Customer Engagement token used to authenticate your credentials. If you omit the token, you must have already created a valid [`PaymentCardReaderSession`](paymentcardreadersession.md) before calling this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/open(using:))*