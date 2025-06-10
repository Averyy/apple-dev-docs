# Revoking API Keys

**Framework**: App Store Connect API

Revoke unused, lost, or compromised private keys.

#### Overview

Revoke an API key immediately if it becomes inactive, lost, or compromised. A revoked API key denies access to the App Store Connect API on your organization’s behalf.

> ❗ **Important**:  Once you revoke an API key, you can’t reinstate it. Revoked keys are displayed for 30 days on the API Keys page under the Revoked heading.

##### Revoking Team Keys

To revoke a team API key, log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) with an Admin account.

1. Select Users and Access, then select the Keys tab.
2. Click Edit next to the list of Active keys.
3. Select the API keys to revoke, and click Revoke Key.
4. Click the Revoke button to confirm.

##### Revoking Individual Keys

There are two ways to revoke an individual API key, depending on your role. Begin both methods by logging in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/).

To revoke keys for another user, as an Admin:

1. Select Users and Access, then select the Keys tab.
2. Click Individual Keys.
3. Click Edit next to the list of Active keys.
4. Select the API keys to revoke, and click Revoke Key.
5. Click the Revoke button to confirm.

To revoke your own key:

1. Go to your user profile.
2. Scroll down to Individual API Key.
3. Click Revoke.
4. Click the Revoke button to confirm.

> 💡 **Tip**:  Admins can prevent a user from creating an Individual Key by removing the Generate Individual API Keys permission.

## See Also

- [Creating API Keys for App Store Connect API](creating-api-keys-for-app-store-connect-api.md)
  Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Identifying Rate Limits](identifying-rate-limits.md)
  Recognize the rate limits that REST API responses provide and handle them in your code.
- [Uploading Assets to App Store Connect](uploading-assets-to-app-store-connect.md)
  Upload screenshots, app previews, attachments for App Review, and routing app coverage files to App Store Connect.
- [App Store Connect API Release Notes](app-store-connect-api-release-notes.md)
  Learn about new features and updates in the App Store Connect API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/revoking-api-keys)*