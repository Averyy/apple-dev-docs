# localizedDisplayName

**Framework**: ManagedSettings  
**Kind**: property

A localized display name for the category.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
let localizedDisplayName: String?
```

#### Discussion

In an extension that provides shield configurations, this property provides the category’s name. When you access this property outside that extension, the value is `nil`. See `ShieldConfigurationDataSource` in the `ManagedSettingsUI` framework for more information.

## See Also

- [let token: ActivityCategoryToken?](activitycategory/token.md)
  An opaque representation of a category of activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/activitycategory/localizeddisplayname)*