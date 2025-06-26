# Automatic Sign-In API

**Framework**: Automatic Sign-In API  
**Kind**: module

Manage sign-in tokens that facilitate single sign-on across the devices of your media streaming service customers from your web server.

**Availability**:
- Automatic Sign-In API 1.0+

## Mentions

- [Signing people in to their media accounts automatically](../videosubscriberaccount/signing-people-in-to-media-apps-automatically.md)

#### Overview

This API works in conjunction with [`Video Subscriber Account`](https://developer.apple.com/documentation/videosubscriberaccount) to manage sign-in tokens from your web server that implement the [`VSUserAccountManager`](https://developer.apple.com/documentation/videosubscriberaccount/vsuseraccountmanager) Automatic Sign-In feature.

> **Note**: For more on Automatic Sign-In for Apple devices, see [`Signing people in to their media accounts automatically`](https://developer.apple.com/documentation/videosubscriberaccount/signing-people-in-to-media-apps-automatically).

#### Authenticate Your Api Calls and Test Using the Sandbox

The Automatic Sign-In API shares authentication and testing steps with the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI). Before issuing calls to this service, perform the setup in [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI). To test your web server during development, see [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI).

## Topics

### Token updates
- [Update Sign-In Token](update-this-token-for-all-associated-users.md)
  Updates a specific sign-in token to a new value.
- [object UpdateAutoSignInTokenRequest](updateautosignintokenrequest.md)
  The request body that contains the old sign-in token and the new sign-in token.
### Token deletion
- [Delete Sign-In Token](delete-this-token-for-all-associated-users.md)
  Deletes a specific sign-in token.
- [object DeleteAutoSignInTokenRequest](deleteautosignintokenrequest.md)
  The request body that contains the sign-in token to be deleted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AutomaticSignInAPI)*