# ShieldSettings.ActivityCategoryPolicy

**Framework**: ManagedSettings  
**Kind**: enum

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

### Shielding Categories
- [ShieldSettings.ActivityCategoryPolicy.none](shieldsettings/activitycategorypolicy/none.md)
  A policy that indicates the device doesn’t shield any content.
- [ShieldSettings.ActivityCategoryPolicy.all(except:)](shieldsettings/activitycategorypolicy/all(except:).md)
  A policy that indicates the device shields all apps and websites, except content that you specify.
- [case specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>>)](shieldsettings/activitycategorypolicy/specific(_:except:).md)
  A policy that indicates the device shields specific categories of activity, with some exceptions.
### Getting the Range
- [static func != (Self, Self) -> Bool](shieldsettings/activitycategorypolicy/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func == (ShieldSettings.ActivityCategoryPolicy<Activity>, ShieldSettings.ActivityCategoryPolicy<Activity>) -> Bool](shieldsettings/activitycategorypolicy/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.
### Default Implementations
- [Equatable Implementations](shieldsettings/activitycategorypolicy/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var applicationCategories: ShieldSettings.ActivityCategoryPolicy<Application>?](shieldsettings/applicationcategories-swift.property.md)
  Categories of apps for the system to cover with a shielding view.
- [static let applicationCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<Application>>](shieldsettings/applicationcategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of apps for the system to cover with a shielding view.
- [var webDomainCategories: ShieldSettings.ActivityCategoryPolicy<WebDomain>?](shieldsettings/webdomaincategories-swift.property.md)
  Categories of websites for the system to cover with a shielding view.
- [static let webDomainCategories: SettingMetadata<ShieldSettings.ActivityCategoryPolicy<WebDomain>>](shieldsettings/webdomaincategories-swift.type.property.md)
  The metadata for the configuration that specifies categories of websites for the system to shield.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy)*