# ActivityCategory

**Framework**: ManagedSettings  
**Kind**: struct

An activity’s category, such as Entertainment or Social.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
struct ActivityCategory
```

## Topics

### Creating a Category
- [init(token: ActivityCategoryToken)](activitycategory/init(token:).md)
  Initializes the representation with the provided token.
### Accessing Category Identifiers
- [let localizedDisplayName: String?](activitycategory/localizeddisplayname.md)
  A localized display name for the category.
- [let token: ActivityCategoryToken?](activitycategory/token.md)
  An opaque representation of a category of activities.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [typealias ActivityCategoryToken](activitycategorytoken.md)
  A token that represents a category of app or website activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/activitycategory)*