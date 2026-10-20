# UserRole

**Framework**: App Store Connect API  
**Kind**: typealias  
**Role**: Type

A string that represents user roles and permissions in App Store Connect.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
string UserRole
```

## Possible Values

- `ACCESS_TO_REPORTS`: **This permission is deprecated.** Permission to download reports associated with a role. The Access To Reports permission is an additional permission for users with the App Manager, Developer, Marketing, or Sales role. If you add this permission, the user has access to all of your apps.
- `ACCOUNT_HOLDER`: Role responsible for entering into legal agreements with Apple. The person who completes program enrollment has the Account Holder role in their Apple Developer account and their App Store Connect account.
- `ADMIN`: Role that serves as a secondary contact for teams and has many of the same responsibilities as the Account Holder role. Admins have access to all apps.
- `APP_MANAGER`: Role that manages all aspects of an app, such as pricing, App Store information, and app development and delivery.
- `CLOUD_MANAGED_APP_DISTRIBUTION`: Permission to submit requests for apps and software that is then signed by a cloud-managed Apple Distribution certificate. App Store Connect automatically creates a certificate if one doesn’t exist. The system grants this permission by default to Account Holder and Admin roles. Account Holder, Admin, and App Manager roles may grant access to this permission to other users with App Manager or Developer roles. This permission requires that the user has access to Certificates, Identifiers & Profiles.
- `CLOUD_MANAGED_DEVELOPER_ID`: Permission to submit requests for apps and software that is then cloud signed by a cloud-managed Developer ID certificate. App Store Connect automatically creates a certificate if one doesn’t exist. The system grants this permission by default to the Account Holder role. The Account Holder may grant access to this permission to users with the Admin role, who may grant it to other Admins. This permission requires that the user has access to Certificates, Identifiers & Profiles.
- `CREATE_APPS`: A permission that enables users with Developer or Marketing roles to create app records.
- `CUSTOMER_SUPPORT`: Role that analyzes and responds to customer reviews on the App Store. If a user has only the Customer Support role, they go straight to the Ratings and Reviews section when they click on an app in My Apps.
- `DEVELOPER`: Role that manages development and delivery of an app.
- `FINANCE`: Role that manages financial information, including reports and tax forms. A user that has this role can view all apps in Payments and Financial Reports, Sales and Trends, and App Analytics.
- `GENERATE_INDIVIDUAL_KEYS`: Permission that allows a person to generate an individual API key.
- `MARKETING`: Role that manages marketing materials and promotional artwork. If an app is in consideration for featuring on the App Store, Apple contacts the user with this role.
- `SALES`: Role that analyzes sales, downloads, and other analytics for the app.

## Mentions

- [Creating and configuring win-back offers](./creating-and-configuring-win-back-offers.md)
- [App Store Connect API 1.4 release notes](./app-store-connect-api-1-4-release-notes.md)
- [App Store Connect API 3.5 release notes](./app-store-connect-api-3-5-release-notes.md)
- [App Store Connect API 4.3 release notes](./app-store-connect-api-4-3-release-notes.md)
- [App Store Connect API 4.4 release notes](./app-store-connect-api-4-4-release-notes.md)
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
- [Creating auto-renewable subscription groups](./creating-auto-renewable-subscription-groups.md)
- [Managing In-App Purchases](./managing-in-app-purchases.md)

#### Discussion

For more information about roles and permissions, see [Program Roles](https://developer.apple.com/support/roles/).

## See Also

### Objects and Data Types
- [object User](./user.md)
  A member of your App Store Connect team, with assigned roles and access to specific apps.
- [object UserUpdateRequest](./userupdaterequest.md)
  The request body you use to update a User.
- [object UserResponse](./userresponse.md)
  The response body for endpoints that read or modify a single App Store Connect team member.
- [object UsersResponse](./usersresponse.md)
  A response containing a list of team members who have access to your App Store Connect account.
- [object UserVisibleAppsLinkagesRequest](./uservisibleappslinkagesrequest.md)
  A request body you use to add or remove visible apps from a user.
- [object UserVisibleAppsLinkagesResponse](./uservisibleappslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userrole)*