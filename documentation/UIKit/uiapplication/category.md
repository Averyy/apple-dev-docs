# UIApplication.Category

**Framework**: UIKit  
**Kind**: enum

Constants that describe the types of apps in the system.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
enum Category
```

#### Overview

Use the values in this enumeration with [`isDefault(_:)`](uiapplication/isdefault(_:).md) (or, in Objective-C, [`defaultStatusForCategory:error:`](uiapplication/defaultstatusforcategory:error:.md)) to find if your app is the person’s default for a category.

## Topics

### Application categories
- [UIApplication.Category.webBrowser](uiapplication/category/webbrowser.md)
  The app is a web browser.
### Initializers
- [init?(rawValue: Int)](uiapplication/category/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func isDefault(UIApplication.Category) throws -> Bool](uiapplication/isdefault(_:).md)
  Reports whether this app is the person’s default app in the given category.
- [UIApplication.CategoryDefaultError](uiapplication/categorydefaulterror.md)
  Errors that can happen when the system checks if your app is the default app in a category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/category)*