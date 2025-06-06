# mapItem

**Framework**: Foundation  
**Kind**: property

Attaches the specified map item to a user activity object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mapItem: MKMapItem! { get set }
```

#### Discussion

Use this property to share a map item’s location information with other apps so that users can benefit from a more contextually integrated experience. For example, if a user views a location in an app that provides restaurant reviews, this property can make the same location available to the user when they switch to an app that helps them make travel plans.

Setting the [`mapItem`](nsuseractivity/mapitem.md) property also populates the user activity object’s [`contentAttributeSet`](nsuseractivity/contentattributeset.md) property. After attaching a map item to a user activity object, you can easily adopt app search by setting the object’s [`isEligibleForSearch`](nsuseractivity/iseligibleforsearch.md) property to [`true`](https://developer.apple.com/documentation/swift/true). To learn more about participating in app search, see [`App Search Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/index.html#//apple_ref/doc/uid/TP40016308).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsuseractivity/mapitem)*