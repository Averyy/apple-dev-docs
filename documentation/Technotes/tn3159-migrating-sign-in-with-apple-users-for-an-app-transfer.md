# TN3159: Migrating Sign in with Apple users for an app transfer

**Framework**: Technotes

Migrate existing Sign in with Apple user identifiers and private email relay addresses by exchanging transfer identifiers from one developer team to another with the user migration info endpoint.

#### Overview

Sign in with Apple allows you to set up a user account in your system, complete with name, verified email address, and unique stable identifiers that allow the user to sign in to your app with their Apple ID. It works on iOS, macOS, tvOS, watchOS, and visionOS, by using the native app’s bundle identifier (or App ID) as its client identifier. You can also add Sign in with Apple to your website or versions of your app running on other platforms by using the Services ID as its client identifier.

A developer team may decide to transfer a Sign in with Apple enabled app when they’ve sold the app to another developer, or want to move it to another App Store Connect account or organization. For Sign in with Apple apps, you have a sixty (60) days transfer period from the date you complete the app transfer. The user migration endpoint is active for both developer accounts—the transferring team and the recipient team–—during this 60-day app transfer period. You may obtain access tokens and generate and/or exchange transfer identifiers during this time for developer team-scoped user identifiers and private email addresses (if applicable).

To guide you through the user migration process, we’ll discuss the most common scenarios for an app transfer:

- Preparing to migrate users for an app transfer
- Migrating users within the 60-day app transfer period
- Migrating users after the 60-day app transfer period

If you’re encountering errors during user migration, see [`TN3107: Resolving Sign in with Apple response errors`](tn3107-resolving-sign-in-with-apple-response-errors.md) to learn more about the underlying cause of common errors. If you are still unable to resolve your errors, please continue to the scenario that matches the state of your app transfer below.

#### Preparing to Migrate Users for an App Transfer

To prepare your team-scoped user data for the recipient for the app transfer, you need to generate a transfer identifier (transfer ID) for each user in your database. If you have grouped your apps for Sign in with Apple, you will need to ungroup them before initiating the transfer. The Services ID associated with a primary App ID that has configured Sign in with Apple will also be transferred. If you don’t want the Service ID to be transferred to the recipient team, [`remove its association`](https://developer.apple.comhttps://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web) before initiating the transfer.

Once the transfer IDs have been generated and the private user data has been prepared for the recipient team, you may initiate your app transfer. For more information about the app transfer process, see [`App Store Connect Help: Transfer an app – Overview of app transfer`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/transfer-an-app/overview-of-app-transfer).

If you have not obtained access tokens or generated transfer identifiers, but have completed your app transfer within 60 days, see [`Migrating users within the 60-day app transfer period`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Migrating-users-within-the-60-day-app-transfer-period.md). Otherwise, see [`Migrating users after the 60-day app transfer period`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Migrating-users-after-the-60-day-app-transfer-period.md) to learn how to proceed with your user migration.

#### Migrating Users Within the 60 Day App Transfer Period

If you are migrating users within the app transfer period, the auth token and user migration info endpoints are active for both developer teams. For teams transferring their app to another team, see [`Transferring existing users to a recipient team`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Transferring-existing-users-to-a-recipient-team.md). For teams receiving a transferred app from another team, see [`Bringing users from the transferring team into your team`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Bringing-users-from-the-transferring-team-into-your-team.md).

#### Migrating Users After the 60 Day App Transfer Period

If you’ve missed the app transfer period, then you’ll need to transfer the app back to the initial team and back to reactivate the auth token and user migrations info endpoints for both developer teams.

For example, if Team A transferred the app to Team B more than 60 days ago, then Team B should transfer the app back to Team A. Once the original transfer has been reversed, Team A should properly prepare for the migration as described in [`Preparing to migrate users for an app transfer`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Preparing-to-migrate-users-for-an-app-transfer.md). Once Team A prepares the transfer IDs and user data for Team B, they should initiate the app transfer to Team B. Then, Team B can exchange transfer IDs for team-scoped user credentials as described in [`Bringing users from the transferring team into your team`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Bringing-users-from-the-transferring-team-into-your-team.md).

#### Transferring Existing Users to a Recipient Team

Please follow the following steps to process the user migration from your team (Team A) to the recipient team (Team B):

1. Team A obtains access token(s)
2. Team A generates transfer identifers
3. Team A initiates app transfer to Team B

For more information about steps above, please see Transferring your apps and users to another team.

> **Note**: If you receive errors while obtaining access tokens or generating transfer identifiers, but have completed your app transfer within 60 days, see [`TN3107: Resolving Sign in with Apple response errors`](tn3107-resolving-sign-in-with-apple-response-errors.md). Otherwise, see [`Migrating users after the 60-day app transfer period`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Migrating-users-after-the-60-day-app-transfer-period.md) to learn how to proceed with your user migration.

If you receive errors while obtaining access tokens or generating transfer identifiers, but have completed your app transfer within 60 days, see [`TN3107: Resolving Sign in with Apple response errors`](tn3107-resolving-sign-in-with-apple-response-errors.md). Otherwise, see [`Migrating users after the 60-day app transfer period`](tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer#Migrating-users-after-the-60-day-app-transfer-period.md) to learn how to proceed with your user migration.

##### 1 Team a Obtains Access Tokens

There are two ways of obtaining access tokens for user migration:

- fetching the access token for the entire developer team; or
- using the access token received for each user when [`Generate and validate tokens`](https://developer.apple.com/documentation/signinwithapplerestapi/generate_and_validate_tokens) after the user authorization.

The request below fetches the access token for Team A. The request also contains the following:

- the client ID for the transferred app or web service; and
- the client secret created by Team A.

```shell
curl -v POST "https://appleid.apple.com/auth/token" \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=client_credentials' \
-d 'scope=user.migration' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET_ISSUED_BY_TEAM_A'
```

You can use this approach to migrate users in batches instead of individually when validating their user session. There is also no rate limiting for this endpoint. To learn more about generating a client secret for your team, please see [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret).

##### 2 Team a Generates Transfer Identifers

The request below uses the access token for Team A, then generates an existing user’s transfer ID for Team B. The request also contains the following:

- the existing user ID for Team A;
- the developer team ID for Team B;
- the client ID for the transferred app or web service; and
- the client secret created by Team A.

```shell
curl -v POST "https://appleid.apple.com/auth/usermigrationinfo" \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Authorization: Bearer ACCESS_TOKEN_FOR_TEAM_A_OR_EXISTING_USER_ID' \
-d 'sub=EXISTING_USER_ID_FOR_TEAM_A' \
-d 'target=DEVELOPER_TEAM_ID_FOR_TEAM_B' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET_ISSUED_BY_TEAM_A'
```

##### 3 Team a Initiates App Transfer to Team B

Once the transfer IDs have been generated and the private user data has been prepared for the recipient team, you may initiate your app transfer. For more information about the app transfer process, see [`App Store Connect Help: Transfer an app – Overview of app transfer`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/transfer-an-app/overview-of-app-transfer).

#### Bringing Users From the Transferring Team Into Your Team

Please follow the following steps to process the user migration from the transferring team (Team A) to your team (Team B):

1. Team B obtains access token(s)
2. Team B exchanges transfer identifers
3. Team B confirms successful user migration

For more information about steps above, please see Bringing new apps and users into your team.

##### 4 Team B Obtains Access Tokens

There are two ways of obtaining access tokens for user migration:

- fetching the access token for the entire developer team; or
- using the access token received for each user when [`Generate and validate tokens`](https://developer.apple.com/documentation/signinwithapplerestapi/generate_and_validate_tokens) after the user authorization.

The request below fetches the access token for Team B. The request also contains the following:

- the client ID for the transferred app or web service; and
- the client secret created by Team B.

```shell
curl -v POST "https://appleid.apple.com/auth/token" \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=client_credentials' \
-d 'scope=user.migration' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET_ISSUED_BY_TEAM_B'
```

You can use this approach to migrate users in batches instead of individually when validating their user session. There is also no rate limiting for this endpoint. To learn more about generating a client secret for your team, please see [`Creating a client secret`](https://developer.apple.com/documentation/AccountOrganizationalDataSharing/creating-a-client-secret).

##### 5 Team B Exchanges Transfer Identifers

The request below uses the access token for Team B, then exchanges the transfer ID provided by Team A. The request also contains the following:

- the transfer ID obtained from Team A;
- the client ID for the transferred app or web service; and
- the client secret created by Team B.

```shell
curl -v POST "https://appleid.apple.com/auth/usermigrationinfo" \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'Authorization: Bearer ACCESS_TOKEN_FOR_TEAM_B_OR_TRANSFER_ID' \
-d 'transfer_sub=TRANSFER_ID_OBTAINED_FROM_TEAM_A' \
-d 'client_id=CLIENT_ID' \
-d 'client_secret=CLIENT_SECRET_ISSUED_BY_TEAM_B'
```

##### 6 Team B Confirms Successful User Migration

Within your app or web service, you can confirm the user migration was successful by checking the credential state of the user. Its value should be [`ASAuthorizationAppleIDProvider.CredentialState.transferred`](https://developer.apple.com/documentation/AuthenticationServices/ASAuthorizationAppleIDProvider/CredentialState/transferred). To learn more about this step, see Confirm the transferred credential state.

#### Revision History

-  Corrected title.
-  First published.

## See Also

- [TN3189: Managing Mail background traffic load](tn3189-managing-mail-background-traffic-load.md)
  Identify iOS Mail background traffic and manage its impact on your IMAP server.
- [TN3187: Migrating to the UIKit scene-based life cycle](tn3187-migrating-to-the-uikit-scene-based-life-cycle.md)
  Update your app to receive scene-based life-cycle events and manage your user interface using scene objects and methods.
- [TN3188: Troubleshooting In-App Purchases availability in the App Store](tn3188-troubleshooting-in-app-purchases-availability-in-the-app-store.md)
  Verify your In-App Purchases are approved and available for sale in the App Store.
- [TN3186: Troubleshooting In-App Purchases availability in the sandbox](tn3186-troubleshooting-in-app-purchases-availability-in-the-sandbox.md)
  Identify common configurations that make your In-App Purchases unavailable in the sandbox environment.
- [TN3185: Troubleshooting In-App Purchases availability in Xcode](tn3185-troubleshooting-in-app-purchases-availability-in-xcode.md)
  Inspect your active StoreKit configuration file for unexpected configurations.
- [TN3182: Adding privacy tracking keys to your privacy manifest](tn3182-adding-privacy-tracking-keys-to-your-privacy-manifest.md)
  Declare the tracking domains you use in your app or third-party SDK in a privacy manifest.
- [TN3183: Adding required reason API entries to your privacy manifest](tn3183-adding-required-reason-api-entries-to-your-privacy-manifest.md)
  Declare the APIs that can potentially fingerprint devices in your app or third-party SDK in a privacy manifest.
- [TN3184: Adding data collection details to your privacy manifest](tn3184-adding-data-collection-details-to-your-privacy-manifest.md)
  Declare the data your app or third-party SDK collects in a privacy manifest.
- [TN3181: Debugging an invalid privacy manifest](tn3181-debugging-invalid-privacy-manifest.md)
  Identify common configurations that cause unsuccessful privacy manifest validation with the App Store.
- [TN3180: Reverting to App Store Server Notifications V1](tn3180-reverting-app-store-server-notifications-v1.md)
  Migrate from version 2 to version 1 of App Store Server Notifications using the Modify an App endpoint.
- [TN3179: Understanding local network privacy](tn3179-understanding-local-network-privacy.md)
  Learn how local network privacy affects your software.
- [TN3178: Checking for and resolving build UUID problems](tn3178-checking-for-and-resolving-build-uuid-problems.md)
  Ensure that every Mach-O image has a UUID, and that every distinct Mach-O image has its own unique UUID.
- [TN3177: Understanding alternate audio track groups in movie files](tn3177-understanding-alternate-audio-track-groups-in-movie-files.md)
  Learn how alternate groups collect audio tracks, and how to choose which audio track to use in your app.
- [TN3111: iOS Wi-Fi API overview](tn3111-ios-wifi-api-overview.md)
  Explore the various Wi-Fi APIs available on iOS and their expected use cases.
- [TN3176: Troubleshooting Apple Pay payment processing issues](tn3176-troubleshooting-apple-pay-payment-processing-issues.md)
  Diagnose errors that occur when processing Apple Pay payments, identify common causes, and explore potential solutions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3159-migrating-sign-in-with-apple-users-for-an-app-transfer)*