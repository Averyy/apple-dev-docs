# App, Book, and Subscription Management

**Framework**: Device Management

Manage apps, books, and subscriptions for your students and employees.

## Topics

### Getting started
- [Getting started with the management API](getting-started-with-the-management-api.md)
  Configure your device management service to handle content and user assignments.
- [Apps and books metadata for organizations](apps-and-books-metadata-for-organizations.md)
  Get metadata for apps and books your organization owns.
### Managing content
- [Managing assets](managing-assets.md)
  Assign and revoke app and book licenses across your organization.
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.
- [Managing users](managing-users.md)
  Register and manage users for your organization’s managed organizational unit.
- [Setting up and assigning content](setting-up-and-assigning-content.md)
  Distribute purchased licenses to managed users through your device management service.
### Common tasks
- [Using paginated endpoints](using-paginated-endpoints.md)
  Traverse large result sets with page-index and cursor-based pagination.
- [Subscribing to notifications](subscribing-to-notifications.md)
  Monitor events for assets, assignments, and users in your organization.
- [Handling error responses](handling-error-responses.md)
  Investigate and resolve service request errors.
### Configuration management
- [Client Config](client-config-4szk1.md)
  Store client-specific information on the server.
- [Service Config](service-config.md)
  Provides the full list of web service URLs, notification types, request limits, and possible error codes.
### Asset management
- [Get Assets](get-assets-4ski1.md)
  Get the set of assets that your organization manages.
- [Associate Assets](associate-assets.md)
  Associate assets with client user IDs and serial numbers.
- [Disassociate Assets](disassociate-assets.md)
  Disassociate assets from client user IDs and serial numbers.
- [Revoke Assets](revoke-assets.md)
  Revoke assets from client user IDs and serial numbers.
- [Get Assignments](get-assignments-9wv1e.md)
  Get the set of current assignments for users or devices.
### Subscription management
- [Enable Subscriptions](enable-subscriptions.md)
  Declare that your device management service supports subscription management.
- [Disable Subscriptions](disable-subscriptions.md)
  Declare that your device management service doesn’t support subscription management.
- [Get Subscriptions](get-subscriptions.md)
  Get the subscriptions that your organization manages.
- [Get Subscription Assignments](get-subscription-assignments.md)
  Get the subscription assignments for users in your organization.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Disassociate Subscriptions](disassociate-subscriptions.md)
  Disassociate subscriptions from client user IDs.
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.
### User management
- [Get Users](get-users-4mwln.md)
  Get information about a set of users.
- [Create Users](create-users.md)
  Create users to assign apps, books, and subscriptions to.
- [Update Users](update-users.md)
  Update details for existing users.
- [Retire Users](retire-users.md)
  Retire users by client user IDs.
### Event management
- [Event Status](events-status.md)
  Retrieve the status of an asynchronous event.
### Objects and data types
- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object UnlimitedResponseAsset](unlimitedresponseasset.md)
  An asset with an unlimited license that the organization owns.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
- [object RequestUser](requestuser.md)
  The requested user in the organization.
- [object ResponseUser](responseuser.md)
  The user in the organization.
- [object ResponseSubscription](responsesubscription.md)
  A subscription with its assignment counts.
- [object ResponseSubscriptionAssignment](responsesubscriptionassignment.md)
  An assignment of a subscription to a user.
- [object SubscriptionCounts](subscriptioncounts.md)
  The subscription assignment counts broken down by assigned and available.
- [object SubscriptionCountsBreakdown](subscriptioncountsbreakdown.md)
  The breakdown of subscription counts by renewing and expiring status.
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
  The request body for adding or removing subscription administrators.
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
  The confirmation response that the server returns after adding or removing subscription administrators.
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
  An administrator for a subscription.
- [object SubscriptionManagementResponse](subscriptionmanagementresponse.md)
  A confirmation response that reports your device management service’s subscription management support.
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
- [object StatusResponse](statusresponse.md)
  The status of an asynchronous event.
### Legacy API
- [App and book management (Legacy)](app-and-book-management-legacy.md)
  Manage apps and books for your students and employees.
- [Upgrading to the new management API](upgrading-to-the-new-management-api.md)
  Migrate from API version 1 to version 2 for improved performance.

## See Also

- [Device assignment](device-assignment.md)
  Manage devices for your students and employees.
- [Roster management](roster-management.md)
  Manage classes for your students and teachers.
- [Apple School Manager and Apple Business APIs](../apple-school-and-business-manager-api/apple-school-and-business-manager-api.md)
  Automate device management actions and access data about devices that enroll using Automated Device Enrollment with the Apple School Manager and Apple Business APIs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/app-book-and-subscription-management)*