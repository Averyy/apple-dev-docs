# ShieldSettings.ActivityCategoryPolicy

**Framework**: Managed Settings  
**Kind**: enum  
**Role**: Enumeration

Policies available for shielding activities based on their category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum ActivityCategoryPolicy<Activity>
```

## Topics

### Shielding categories
- [ShieldSettings.ActivityCategoryPolicy.none](./activitycategorypolicy/none.md)
  A policy that indicates the device doesn’t shield any content.
- [ShieldSettings.ActivityCategoryPolicy.all(except:)](./activitycategorypolicy/all%28except%29.md)
  A policy that indicates the device shields all apps and websites, except content that you specify.
- [case specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>>)](./activitycategorypolicy/specific%28_,except%29.md)
  A policy that indicates the device shields specific categories of activity, with some exceptions.
### Comparing category policies
- [static func == (ShieldSettings.ActivityCategoryPolicy<Activity>, ShieldSettings.ActivityCategoryPolicy<Activity>) -> Bool](./activitycategorypolicy/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Blocking categories of apps and websites
- [var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?](./applicationcategories-swift.property.md)
  Categories of apps for the system to cover with a shielding view.
- [static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>](./applicationcategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.
- [var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?](./webdomaincategories-swift.property.md)
  Categories of websites for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](./webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy)*