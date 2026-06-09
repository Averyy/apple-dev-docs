# Sandbox Testers

**Framework**: App Store Connect API

Manage sandbox testers on your App Store Connect team.

#### Overview

The `sandboxTesters` resource represents a Sandbox Apple Account, which is an account you use to test your app in the sandbox environment. Using this resource you can read and modify Sandbox Apple Accounts and their data. Use App Store Connect to create or delete Sandbox Apple Account. For more information, see [`Create Sandbox Apple Accounts`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids). For more information about testing in-app purchase in the sandbox environment, see [`Overview of testing in sandbox`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/overview-of-testing-in-sandbox).

## Topics

### Sandbox Tester Lookup and Modification
- [List sandbox testers](get-v2-sandboxtesters.md)
  Get a list of Sandbox Testers for your team.
- [Modify a sandbox tester](patch-v2-sandboxtesters-_id_.md)
  Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.
- [Clear purchase history for a sandbox tester](post-v2-sandboxtestersclearpurchasehistoryrequest.md)
  Remove purchase history from a Sandbox Apple Account.
### Objects
- [object SandboxTesterV2Response](sandboxtesterv2response.md)
  The response body for endpoints that read or modify a single sandbox Apple ID for testing.
- [object SandboxTesterV2UpdateRequest](sandboxtesterv2updaterequest.md)
  The request body you use to update a sandbox tester v2update request.
- [object SandboxTestersClearPurchaseHistoryRequestV2](sandboxtestersclearpurchasehistoryrequestv2.md)
  A batch request to reset the in-app purchase and subscription history for one or more sandbox Apple IDs.
- [object SandboxTestersClearPurchaseHistoryRequestV2CreateRequest](sandboxtestersclearpurchasehistoryrequestv2createrequest.md)
  The request body you use to create a request to clear sandbox tester purchase history.
- [object SandboxTestersClearPurchaseHistoryRequestV2Response](sandboxtestersclearpurchasehistoryrequestv2response.md)
  A response confirming that the purchase history for sandbox testers was cleared.
- [object SandboxTestersV2Response](sandboxtestersv2response.md)
  The response body for endpoints that list sandbox Apple IDs used for testing.
- [object SandboxTesterV2](sandboxtesterv2.md)
  A sandbox Apple ID you use to test in-app purchases and subscriptions in the Xcode sandbox environment.

## See Also

- [Users](users.md)
  Manage users on your App Store Connect team.
- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/sandbox-testers)*