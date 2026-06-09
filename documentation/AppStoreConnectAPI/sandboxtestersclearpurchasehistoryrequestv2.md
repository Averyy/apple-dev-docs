# SandboxTestersClearPurchaseHistoryRequestV2

**Framework**: App Store Connect API  
**Kind**: dictionary

A batch request to reset the in-app purchase and subscription history for one or more sandbox Apple IDs.

**Availability**:
- App Store Connect API 2.2+

## Declaration

```swift
object SandboxTestersClearPurchaseHistoryRequestV2
```

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object SandboxTesterV2Response](sandboxtesterv2response.md)
  The response body for endpoints that read or modify a single sandbox Apple ID for testing.
- [object SandboxTesterV2UpdateRequest](sandboxtesterv2updaterequest.md)
  The request body you use to update a sandbox tester v2update request.
- [object SandboxTestersClearPurchaseHistoryRequestV2CreateRequest](sandboxtestersclearpurchasehistoryrequestv2createrequest.md)
  The request body you use to create a request to clear sandbox tester purchase history.
- [object SandboxTestersClearPurchaseHistoryRequestV2Response](sandboxtestersclearpurchasehistoryrequestv2response.md)
  A response confirming that the purchase history for sandbox testers was cleared.
- [object SandboxTestersV2Response](sandboxtestersv2response.md)
  The response body for endpoints that list sandbox Apple IDs used for testing.
- [object SandboxTesterV2](sandboxtesterv2.md)
  A sandbox Apple ID you use to test in-app purchases and subscriptions in the Xcode sandbox environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/sandboxtestersclearpurchasehistoryrequestv2)*