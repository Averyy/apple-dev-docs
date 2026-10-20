# UIApplication.CategoryDefaultError

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Errors that can happen when the system checks if your app is the default app in a category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
struct CategoryDefaultError
```

## Topics

### Getting information about the error
- [UIApplication.CategoryDefaultError.Code](./categorydefaulterror/code.md)
  An enumeration of reasons an error happens when the system discovers whether your app is the default in a category.
- [static let retryAvailableDateErrorKey: String](./categorydefaulterror/retryavailabledateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [static let statusLastProvidedDateErrorKey: String](./categorydefaulterror/statuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.
### Errors when discovering if an app is the default in a category
- [static var errorDomain: String](./categorydefaulterror/errordomain.md)
  A string that indicates that an error happened when the system attempted to determine if your app is the default in a category.
- [static var rateLimited: UIApplication.CategoryDefaultError.Code](./categorydefaulterror/ratelimited.md)
  An error code that indicates your app requested its status too frequently.

## Relationships

### Conforms To
- [CustomNSError](../../Foundation/customnserror.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Discovering if your app is the default app in a category
- [func isDefault(UIApplication.Category) throws -> Bool](./isdefault%28_%29.md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplication.Category](./category.md)
  Constants that describe the types of apps in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror)*