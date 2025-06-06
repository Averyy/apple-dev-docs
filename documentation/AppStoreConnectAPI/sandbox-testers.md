# Sandbox Testers

**Framework**: App Store Connect API

Manage sandbox testers on your App Store Connect team.

#### Overview

The `sandboxTesters` resource represents a Sandbox Apple Account, which is an account you use to test your app in the sandbox environment. Using this resource you can read and modify Sandbox Apple Accounts and their data. Use App Store Connect to create or delete Sandbox Apple Account. For more information, see [`Create Sandbox Apple Accounts`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/create-sandbox-apple-ids). For more information about testing in-app purchase in the sandbox environment, see [`Overview of testing in sandbox`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-in-app-purchases/overview-of-testing-in-sandbox).

## Topics

### Sandbox Tester Lookup and Modification
- [List Sandbox Testers](get-v2-sandboxtesters.md)
  Get a list of Sandbox Testers for your team.
- [Modify a Sandbox Tester](patch-v2-sandboxtesters-_id_.md)
  Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.
- [Clear Purchase History for a Sandbox Tester](post-v2-sandboxtestersclearpurchasehistoryrequest.md)
  Remove purchase history from a Sandbox Apple Account.
### Objects
- [object SandboxTesterV2Response](sandboxtesterv2response.md)
- [object SandboxTesterV2UpdateRequest](sandboxtesterv2updaterequest.md)
- [object SandboxTestersClearPurchaseHistoryRequestV2](sandboxtestersclearpurchasehistoryrequestv2.md)
- [object SandboxTestersClearPurchaseHistoryRequestV2CreateRequest](sandboxtestersclearpurchasehistoryrequestv2createrequest.md)
- [object SandboxTestersClearPurchaseHistoryRequestV2Response](sandboxtestersclearpurchasehistoryrequestv2response.md)
- [object SandboxTestersV2Response](sandboxtestersv2response.md)
- [object SandboxTesterV2](sandboxtesterv2.md)

## See Also

- [Users](users.md)
  Manage users on your App Store Connect team.
- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/sandbox-testers)*