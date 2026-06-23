# requestAddress(for:fields:message:)

**Framework**: ProximityReader  
**Kind**: method

Opens a form so that the customer can share the postal address and additionally collect email address and phone number.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func requestAddress(for purpose: CustomerEngagementSession.Purpose? = nil, fields: [CustomerEngagementSession.Field], message: String? = nil) async throws -> CustomerEngagement.Address
```

#### Return Value

[`CustomerEngagement.Address`](customerengagement/address.md) with postal address and contact information shared by the customer.

#### Discussion

For example, email and phone number can be used for delivery notification.

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails.

## Parameters

- `purpose`: An optional enum of pre-defined purpose of the form, for example `.shipping`.
- `fields`: An array of optional contact field types on the form. Only `.emailAddress` and `.phoneNumber` types are supported.
- `message`: A multi-line message text below the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestaddress(for:fields:message:))*