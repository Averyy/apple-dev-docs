# Creating API Keys for App Store Connect API

**Framework**: App Store Connect API

Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.

#### Overview

The App Store Connect API requires a JSON Web Token (JWT) to authorize each request you make to the API. You generate JWTs using an API key downloaded from App Store Connect.

An API key has two parts: a public portion that Apple keeps, and a private key that you download. You can use the private key to sign tokens that authorize access to your data in App Store Connect and the Apple Developer website.

There are two types of API keys:

> ❗ **Important**:  Secure your private keys as you do for other credentials, such as usernames and passwords. If you suspect a private key is compromised, immediately revoke the key in App Store Connect. See [`Revoking API Keys`](revoking-api-keys.md) for details.

 Secure your private keys as you do for other credentials, such as usernames and passwords. If you suspect a private key is compromised, immediately revoke the key in App Store Connect. See [`Revoking API Keys`](revoking-api-keys.md) for details.

App Store Connect API keys are unique to the App Store Connect API and you can’t use them for other Apple services.

##### Generate a Team Key and Assign It a Role

When you create an API key, assign it a role that determines the key’s access to areas of the App Store Connect API and permissions for performing tasks. For example, keys with the Admin role have broad permissions and can do things like create new users and delete users. Team API keys can access all apps, regardless of their role. The roles that apply to keys are the same roles that apply to users on your team; for more information, see [`Program Roles`](https://developer.apple.comhttps://developer.apple.com/support/roles/).

> **Note**:  Team keys give access that’s not isolated to a single app, but individual key access is tied to the apps and permissions of the user.

 Team keys give access that’s not isolated to a single app, but individual key access is tied to the apps and permissions of the user.

To generate team keys, you must have an Admin account in App Store Connect. You can generate multiple API keys with any roles you choose.

To generate a team API key to use with the App Store Connect API, log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) and:

1. Select Users and Access, and then select the Integrations tab.
2. Select App Store Connect API in the left column.
3. Make sure the Team Keys tab is selected.
4. Click Generate API Key or the Add (+) button.
5. Enter a name for the key. The name is for your reference only and isn’t part of the key itself.
6. Under Access, select the role for the key.
7. Click Generate.

The new key’s name, key ID, a download link, and other information appears on the page.

##### Download and Store a Team Private Key

Once you generate your API key, you can download the private half of the key. The private key is available for download a single time, to begin log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) and:

1. Select Users and Access, and then select the Integrations tab.
2. Select App Store Connect API in the left column.
3. Select Team Keys if it is not already selected.
4. Click Download API Key link next to the new API key.

The download link only appears if you haven’t downloaded the private key. Apple doesn’t keep a copy of the private key.

> ❗ **Important**:  Keep your API keys secure and private. Don’t share your keys, store keys in a code repository, or include keys in client-side code. If the key becomes lost or compromised, remember to revoke it immediately. See [`Revoking API Keys`](revoking-api-keys.md) for more information.

 Keep your API keys secure and private. Don’t share your keys, store keys in a code repository, or include keys in client-side code. If the key becomes lost or compromised, remember to revoke it immediately. See [`Revoking API Keys`](revoking-api-keys.md) for more information.

##### Generate an Individual Key

To generate an individual API key, which has access and permissions of the associated user, for the App Store Connect API, log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) and:

1. Go to your user profile.
2. Scroll down to Individual API Key.
3. Click Generate API Key.

The key ID, a download link, and other information appears on the page.

> **Note**:  If you don’t have the Generate Individual API Keys permission, the Generate API Key button won’t show on your profile. A team Admin can grant you this permission.

 If you don’t have the Generate Individual API Keys permission, the Generate API Key button won’t show on your profile. A team Admin can grant you this permission.

##### Download and Store an Individual Private Key

Once you’ve generated your API key, you can download the private half of the key. The private key is available for download a single time, to begin log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/) and:

1. Go to your user profile.
2. Scroll down to Individual API Key.
3. Click Download API Key link.

The download link only appears if you haven’t downloaded the private key. Apple doesn’t keep a copy of the private key.

## See Also

- [Generating Tokens for API Requests](generating-tokens-for-api-requests.md)
  Create JSON Web Tokens (JWTs) signed with your private key to authorize API requests.
- [Revoking API Keys](revoking-api-keys.md)
  Revoke unused, lost, or compromised private keys.
- [Identifying Rate Limits](identifying-rate-limits.md)
  Recognize the rate limits that REST API responses provide and handle them in your code.
- [Uploading Assets to App Store Connect](uploading-assets-to-app-store-connect.md)
  Upload screenshots, app previews, attachments for App Review, and routing app coverage files to App Store Connect.
- [App Store Connect API Release Notes](app-store-connect-api-release-notes.md)
  Learn about new features and updates in the App Store Connect API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/creating-api-keys-for-app-store-connect-api)*