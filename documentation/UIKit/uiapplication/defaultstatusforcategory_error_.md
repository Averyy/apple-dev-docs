# defaultStatusForCategory:error:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Reports whether this app is the person’s default app in the given category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
- (UIApplicationCategoryDefaultStatus) defaultStatusForCategory:(UIApplicationCategory) category error:(NSError **) error;
```

## Return Value

If the system could determine the status of the app, this method returns [`UIApplicationCategoryDefaultStatusIsDefault`](../uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusisdefault.md) if the app is the default app in the category, and [`UIApplicationCategoryDefaultStatusNotDefault`](../uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusnotdefault.md) otherwise. If the system couldn’t determine the status, or the app has exceeded the threshold rate for calling this method, it returns [`UIApplicationCategoryDefaultStatusUnavailable`](../uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusunavailable.md) and supplies more information about the problem in `error`.

## Discussion

To reduce the likelihood that users will face continuous requests to set a browser as their default, this API will only tell the browser app if it is the default once per year. If you call the method too frequently, it throws an error with the domain [`UIApplicationCategoryDefaultErrorDomain`](../uiapplicationcategorydefaulterrordomain.md) and the code [`rateLimited`](./categorydefaulterror/ratelimited.md). The error’s info dictionary contains these keys:

- **[`UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey`](../uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md)**: The date at which the app most recently received a [`UIApplicationCategoryDefaultStatusIsDefault`](../uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusisdefault.md) or [`UIApplicationCategoryDefaultStatusNotDefault`](../uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusnotdefault.md) response from this method.
- **[`UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey`](../uiapplicationcategorydefaultretryavailabilitydateerrorkey.md)**: The date at which the app can next request an updated response.

## Parameters

- `category`: The type of app for which you test whether your app is the default.
- `error`: If an error occurs, upon return contains an [`NSError`](../../Foundation/nserror.md) object that describes the problem. If you are not interested in possible errors, pass in `NULL`.

## See Also

### Discovering if your app is the default app in a category
- [UIApplicationCategoryDefaultStatus](../uiapplicationcategorydefaultstatus.md)
  The default status of an application for some category.
- [UIApplication.Category](./category.md)
  Constants that describe the types of apps in the system.
- [UIApplicationCategoryDefaultErrorDomain](../uiapplicationcategorydefaulterrordomain.md)
  A string that identifies errors the system encounters when it determines if your app is the default in a category.
- [UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey](../uiapplicationcategorydefaultretryavailabilitydateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey](../uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/defaultstatusforcategory:error:)*