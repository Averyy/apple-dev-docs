# Revoking API Keys

**Framework**: Enterprise Program API

Revoke unused, lost, or compromised private keys.

#### Overview

Revoke an API key immediately if it becomes inactive, lost, or compromised. A revoked API key denies access to the Enterprise Program API on your organization’s behalf.

> ❗ **Important**:  Once you revoke an API key, you can’t reinstate it. Revoked keys are displayed for 30 days on the Integrations page under the Revoked heading.

 Once you revoke an API key, you can’t reinstate it. Revoked keys are displayed for 30 days on the Integrations page under the Revoked heading.

##### Revoking Enterprise Program Keys

To revoke a team API key, log in to the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com) with an Admin account.

1. Select Users and Access, then select the Integrations tab.
2. Click Edit next to the list of Active keys.
3. Select the API keys to revoke, and click Revoke Key.
4. Click the Revoke button to confirm.

## See Also

- [Creating API Keys for Enterprise Program API](creating-api-keys-for-enterprise-program-api.md)
  Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Identifying Rate Limits](identifying-rate-limits.md)
  Recognize the rate limits that REST API responses provide and handle them in your code.
- [Enterprise Program API Release Notes](enterprise-api-release-notes.md)
  Learn about new features and updates in the Enterprise Program API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/revoking-api-keys)*