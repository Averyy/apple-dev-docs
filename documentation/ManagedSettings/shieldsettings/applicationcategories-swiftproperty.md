# applicationCategories

**Framework**: ManagedSettings  
**Kind**: property

Categories of apps for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>? { get set }
```

#### Discussion

When the user launches an application in one of these categories, the system calls your extension that customizes the shield’s appearance. When the user taps on a button the shield displays, the system calls your extension that handles user actions. Your app is exempt from `.all`. If your app doesn’t provide a list of categories to shield, this value is `nil`. Your app can shield up to 50 category tokens and specify up to 50 application tokens exceptions at once.

## See Also

- [ShieldSettings.ActivityCategoryPolicy](shieldsettings/activitycategorypolicy.md)
  Policies available for shielding activities based on their category.
- [static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>](shieldsettings/applicationcategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.
- [var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?](shieldsettings/webdomaincategories-swift.property.md)
  Categories of websites for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](shieldsettings/webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/applicationcategories-swift.property)*