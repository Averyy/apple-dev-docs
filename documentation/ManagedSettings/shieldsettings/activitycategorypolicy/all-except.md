# ShieldSettings.ActivityCategoryPolicy.all(except:)

**Framework**: ManagedSettings  
**Kind**: case

A policy that indicates the device shields all apps and websites, except content that you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case all(except: Set<Token<Activity>> = [])
```

#### Discussion

Your app can specify up to 50 application or web domain tokens exceptions at once.

## See Also

- [ShieldSettings.ActivityCategoryPolicy.none](shieldsettings/activitycategorypolicy/none.md)
  A policy that indicates the device doesn’t shield any content.
- [case specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>>)](shieldsettings/activitycategorypolicy/specific(_:except:).md)
  A policy that indicates the device shields specific categories of activity, with some exceptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy/all(except:))*