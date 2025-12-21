# App Store Connect API

**Framework**: App Store Connect API  
**Kind**: module

Automate the tasks you perform on the Apple Developer website and in App Store Connect.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)

#### Overview

The App Store Connect API is a REST API that enables the automation of actions you take in App Store Connect. Click [`OpenAPI specification`](https://developer.apple.comhttps://developer.apple.com/sample-code/app-store-connect/app-store-connect-openapi-specification.zip) to download the specification file.

Calls to the API require JSON Web Tokens (JWT) for authorization; you obtain keys to create the tokens from your organization’s App Store Connect account. See [`Creating API Keys for App Store Connect API`](creating-api-keys-for-app-store-connect-api.md) to create your keys and tokens.

> ❗ **Important**:  Changes you make using the App Store Connect API affect the production data you use for development and distribution.

The API provides resources to automate these areas of App Store Connect:

-  Manage in-app purchases and auto-renewable subscriptions for your app.
-  Manage beta builds of your app, testers, and groups.
-  Read Xcode Cloud data, manage workflows, and start builds.
-  Send invitations for users to join your team. Adjust their level of access or remove users.
-  Manage bundle IDs, capabilities, signing certificates, devices, and provisioning profiles.
-  Create new versions, manage App Store information, and submit your app to the App Store.
-  Create an App Clip and manage App Clip experiences.
-  Download sales and financial reports.
-  Download aggregate metrics and diagnostics for App Store versions of your app.
-  Get the customer reviews for your app and manage your responses to the customer reviews.

The App Store Connect API returns responses from resources that are consistent JSON data and contain links to additional related resources. Use these relationships to navigate to the related resources—for example, to find beta testers within specific beta groups in TestFlight. Apply filtering to requests on specific resources to refine the response.

## Topics

### Essentials
- [Creating API Keys for App Store Connect API](creating-api-keys-for-app-store-connect-api.md)
  Create API keys to sign JSON Web Tokens (JWTs) and authorize API requests.
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
### App Store
- [App Store](app-store.md)
  Manage all aspects of your app, App Clips, in-app purchases, and customer reviews in the App Store.
### TestFlight
- [Prerelease Versions and Beta Testers](prerelease-versions-and-beta-testers.md)
  Manage your beta testing program, including beta testers and groups, apps, App Clips, and builds.
### Game Center
- [Game Center](game-center.md)
  Manage Game Center data and configurations for your apps.
### Provisioning
- [Bundle IDs](bundle-ids.md)
  Manage the bundle IDs that uniquely identify your apps.
- [Bundle ID Capabilities](bundle-id-capabilities.md)
  Manage the app capabilities for a bundle ID.
- [Certificates](certificates.md)
  Create, download, and revoke signing certificates for app development and distribution.
- [Devices](devices.md)
  Register devices for development and testing.
- [Profiles](profiles.md)
  Create, delete, and download provisioning profiles that enable app installations for development and distribution.
- [Merchant ID](merchantids.md)
  Manage your merchant ID for Apple Pay.
- [Pass type Ids](pass-type-id.md)
  Create, download, and revoke pass type ids for app development and distribution.
### Xcode Cloud
- [Xcode Cloud Workflows and Builds](xcode-cloud-workflows-and-builds.md)
  Automate reading Xcode Cloud data, managing workflows, and starting builds.
### Webhooks
- [Webhook notifications](webhook-notifications.md)
  Manage notifications from App Store about your apps and their statuses.
### Reporting
- [Sales and Finance](sales-and-finance.md)
  Download your sales and financial reports.
- [Power and Performance Metrics and Logs](power-and-performance-metrics-and-logs.md)
  Get power and performance metrics, logs, and signatures.
- [Analytics](analytics.md)
  Get data about your apps and usage.
### Users and Access
- [Users](users.md)
  Manage users on your App Store Connect team.
- [User Invitations](user-invitations.md)
  Email invitations to join your App Store Connect team.
- [Sandbox Testers](sandbox-testers.md)
  Manage sandbox testers on your App Store Connect team.
### Error Handling
- [Interpreting and Handling Errors](interpreting-and-handling-errors.md)
  Learn how the App Store Connect API returns errors and handle them in your code.
### Paging
- [Large Data Sets](large-data-sets.md)
  Retrieve large data sets with paging information.
### Alternative App Distribution
- [Alternative Marketplaces and Web Distribution](alternative-marketplaces-and-web-distribution.md)
  Manage keys, packages, and search for alternative app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppStoreConnectAPI)*