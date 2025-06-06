# ActivityCategoryToken

**Framework**: ManagedSettings  
**Kind**: typealias

A token that represents a category of app or website activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
typealias ActivityCategoryToken = Token<ActivityCategory>
```

#### Discussion

Use `ActivityCategoryToken` to restrict and filter device applications without access to personal user data. [`FamilyActivitySelection`](https://developer.apple.com/documentation/FamilyControls/FamilyActivitySelection) provides tokens that devices within the same Family Sharing group can use to identify applications.

## See Also

- [struct ActivityCategory](activitycategory.md)
  An activity’s category, such as Entertainment or Social.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/activitycategorytoken)*