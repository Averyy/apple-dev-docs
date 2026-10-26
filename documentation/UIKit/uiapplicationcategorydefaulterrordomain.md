# UIApplicationCategoryDefaultErrorDomain

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

A string that identifies errors the system encounters when it determines if your app is the default in a category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```c
extern NSErrorDomain const UIApplicationCategoryDefaultErrorDomain;
```

## See Also

### Discovering if your app is the default app in a category
- [- defaultStatusForCategory:error:](./uiapplication/defaultstatusforcategory_error_.md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplicationCategoryDefaultStatus](./uiapplicationcategorydefaultstatus.md)
  The default status of an application for some category.
- [UIApplication.Category](./uiapplication/category.md)
  Constants that describe the types of apps in the system.
- [UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey](./uiapplicationcategorydefaultretryavailabilitydateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey](./uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationcategorydefaulterrordomain)*