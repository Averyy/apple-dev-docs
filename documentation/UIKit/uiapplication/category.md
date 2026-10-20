# UIApplication.Category

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the types of apps in the system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
enum Category
```

```c
enum UIApplicationCategory : NSInteger;
```

#### Overview

Use the values in this enumeration with [`isDefault(_:)`](./isdefault%28_%29.md) (or, in Objective-C, [`defaultStatusForCategory:error:`](./defaultstatusforcategory_error_.md)) to find if your app is the person’s default for a category.

## Topics

### Application categories
- [UIApplication.Category.webBrowser](./category/webbrowser.md)
  The app is a web browser.
### Initializers
- [init?(rawValue: Int)](./category/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Discovering if your app is the default app in a category
- [func isDefault(UIApplication.Category) throws -> Bool](./isdefault%28_%29.md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplication.CategoryDefaultError](./categorydefaulterror.md)
  Errors that can happen when the system checks if your app is the default app in a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/category)*