# applicationCategories

**Framework**: ManagedSettings  
**Kind**: property

The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>
```

#### Discussion

The default value is [`ShieldSettings.ActivityCategoryPolicy.none`](shieldsettings/activitycategorypolicy/none.md).

## See Also

- [ShieldSettings.ActivityCategoryPolicy](shieldsettings/activitycategorypolicy.md)
  Policies available for shielding activities based on their category.
- [var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?](shieldsettings/applicationcategories-swift.property.md)
  Categories of apps for the system to cover with a shielding view.
- [var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?](shieldsettings/webdomaincategories-swift.property.md)
  Categories of websites for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](shieldsettings/webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/applicationcategories-swift.type.property)*