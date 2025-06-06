# ShieldSettings.ActivityCategoryPolicy.specific(_:except:)

**Framework**: ManagedSettings  
**Kind**: case

A policy that indicates the device shields specific categories of activity, with some exceptions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>> = [])
```

#### Discussion

List categories you want to shield in the first parameter. Use the `except` parameter to specify apps and websites not to shield, even if they’re in the categories that you list. Your app can shield up to 50 category tokens and specify up to 50 application or web domain tokens exceptions at once.

## See Also

- [ShieldSettings.ActivityCategoryPolicy.none](shieldsettings/activitycategorypolicy/none.md)
  A policy that indicates the device doesn’t shield any content.
- [ShieldSettings.ActivityCategoryPolicy.all(except:)](shieldsettings/activitycategorypolicy/all(except:).md)
  A policy that indicates the device shields all apps and websites, except content that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy/specific(_:except:))*