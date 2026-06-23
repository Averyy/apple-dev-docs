# requestCustomerInfo(for:fields:message:)

**Framework**: ProximityReader  
**Kind**: method

Opens a form so that the customer can share the contact information.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func requestCustomerInfo(for purpose: CustomerEngagementSession.Purpose? = nil, fields: [CustomerEngagementSession.Field], message: String? = nil) async throws -> CustomerEngagement.CustomerInfo
```

#### Return Value

[`CustomerEngagement.CustomerInfo`](customerengagement/customerinfo.md) contact information shared by the customer.

#### Discussion

If the `fields` array contains `pass` and a matching `passTypeIdentifier` , it displays the Wallet pass in full screen for the customer to confirm.

> **Note**: [`CustomerEngagementSession.Error`](customerengagementsession/error.md) if the request fails. Note: The merchant is responsible for obtaining appropriate consent and maintaining compliant privacy notices for personal information collected through this session.

## Parameters

- `purpose`: An optional enum of pre-defined purpose of the form, for example `.checkIn`. The `purpose`` parameter supports `.checkIn`and`.receipt`.
- `fields`: An array of contact field types on the form.
- `message`: A multi-line message text below the title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestcustomerinfo(for:fields:message:))*