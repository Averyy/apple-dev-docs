# UIApplicationCategoryDefaultStatus

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The default status of an application for some category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```c
enum UIApplicationCategoryDefaultStatus : NSInteger;
```

## Topics

### Enumeration Cases
- [UIApplicationCategoryDefaultStatusIsDefault](./uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusisdefault.md)
  The application is the default for the category.
- [UIApplicationCategoryDefaultStatusNotDefault](./uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusnotdefault.md)
  The application is not the default for the category.
- [UIApplicationCategoryDefaultStatusUnavailable](./uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusunavailable.md)
  The status was not available. This is an error condition and the returned error object has more information.

## See Also

### Discovering if your app is the default app in a category
- [- defaultStatusForCategory:error:](./uiapplication/defaultstatusforcategory_error_.md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplication.Category](./uiapplication/category.md)
  Constants that describe the types of apps in the system.
- [UIApplicationCategoryDefaultErrorDomain](./uiapplicationcategorydefaulterrordomain.md)
  A string that identifies errors the system encounters when it determines if your app is the default in a category.
- [UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey](./uiapplicationcategorydefaultretryavailabilitydateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey](./uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationcategorydefaultstatus)*