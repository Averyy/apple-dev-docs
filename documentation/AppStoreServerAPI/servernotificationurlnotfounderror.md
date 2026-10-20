# ServerNotificationURLNotFoundError

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the App Store server couldn’t find a notifications URL for your app in the environment.

**Availability**:
- App Store Server API 1.5+

## Declaration

```
object ServerNotificationURLNotFoundError
```

## Properties

- `errorCode` (int64): **Allowed Values**: `4040007`
- `errorMessage` (string): For more information about configuring App Store Server Notifications in App Store Connect, see [Enter a URL for App Store server notifications](https://help.apple.com/app-store-connect/#/dev0067a330b). Check that you’ve configured a server notifications URL for the production environment or sandbox enviroment, whichever you’re using.

  **Allowed Values**: `No App Store Server Notification URL found for provided app. Check that a URL is configured in App Store Connect for this environment.`

## See Also

### Notification test and history errors
- [object InvalidEndDateError](./invalidenddateerror.md)
  An error that indicates the end date is invalid.
- [object InvalidNotificationTypeError](./invalidnotificationtypeerror.md)
  An error that indicates the notification type or subtype is invalid.
- [object InvalidPaginationTokenError](./invalidpaginationtokenerror.md)
  An error that indicates the pagination token is invalid.
- [object InvalidStartDateError](./invalidstartdateerror.md)
  An error that indicates the start date is invalid.
- [object InvalidTestNotificationTokenError](./invalidtestnotificationtokenerror.md)
  An error that indicates the test notification token is invalid.
- [object InvalidInAppOwnershipTypeError](./invalidinappownershiptypeerror.md)
  An error that indicates an invalid in-app ownership type parameter.
- [object InvalidProductIdError](./invalidproductiderror.md)
  An error that indicates the product ID parameter is invalid.
- [object InvalidProductTypeError](./invalidproducttypeerror.md)
  An error that indicates the product type parameter is invalid.
- [object InvalidSortError](./invalidsorterror.md)
  An error that indicates the sort parameter is invalid.
- [object InvalidSubscriptionGroupIdentifierError](./invalidsubscriptiongroupidentifiererror.md)
  An error that indicates the subscription group identifier is invalid.
- [object MultipleFiltersSuppliedError](./multiplefilterssuppliederror.md)
  An error that indicates the request is invalid because it has too many applied constraints.
- [object PaginationTokenExpiredError](./paginationtokenexpirederror.md)
  An error that indicates the pagination token expired.
- [object StartDateAfterEndDateError](./startdateafterenddateerror.md)
  An error that indicates the end date precedes the start date, or the two dates are equal.
- [object StartDateTooFarInPastError](./startdatetoofarinpasterror.md)
  An error that indicates the start date is earlier than the earliest allowed date.
- [object TestNotificationNotFoundError](./testnotificationnotfounderror.md)
  An error that indicates the test notification token is expired or the test notification status isn’t available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/servernotificationurlnotfounderror)*