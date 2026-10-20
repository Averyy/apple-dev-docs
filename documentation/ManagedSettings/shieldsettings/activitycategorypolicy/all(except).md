# ShieldSettings.ActivityCategoryPolicy.all(except:)

**Framework**: Managed Settings  
**Kind**: case  
**Role**: Case

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

### Shielding categories
- [ShieldSettings.ActivityCategoryPolicy.none](./none.md)
  A policy that indicates the device doesn’t shield any content.
- [case specific(Set<ActivityCategoryToken>, except: Set<Token<Activity>>)](./specific%28_,except%29.md)
  A policy that indicates the device shields specific categories of activity, with some exceptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/shieldsettings/activitycategorypolicy/all(except:))*