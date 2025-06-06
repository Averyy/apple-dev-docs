# ActivityCategory

**Framework**: ManagedSettings  
**Kind**: struct

An activity’s category, such as Entertainment or Social.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

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
### Comparing Categories
- [static func == (ActivityCategory, ActivityCategory) -> Bool](activitycategory/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](activitycategory/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [func hash(into: inout Hasher)](activitycategory/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](activitycategory/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](activitycategory/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [typealias ActivityCategoryToken](activitycategorytoken.md)
  A token that represents a category of app or website activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/activitycategory)*