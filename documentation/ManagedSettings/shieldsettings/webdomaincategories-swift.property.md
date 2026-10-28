# webDomainCategories

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Instance Property

Categories of websites for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>? { get set }
```

## Discussion

When the user visits a website in one of these categories, the system calls your extension that customizes the shield’s appearance. When the user taps on a button the shield displays, the system calls your extension that handles user actions. If your app doesn’t provide a list of website categories to shield, this value is `nil`. Your app can shield up to 50 category tokens and specify up to 50 web domain tokens exceptions at once.

## See Also

### Blocking categories of apps and websites
- [ShieldSettings.ActivityCategoryPolicy](./activitycategorypolicy.md)
  Policies available for shielding activities based on their category.
- [var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?](./applicationcategories-swift.property.md)
  Categories of apps for the system to cover with a shielding view.
- [static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>](./applicationcategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](./webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/webdomaincategories-swift.property)*