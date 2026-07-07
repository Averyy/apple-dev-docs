# supportsNavigation

**Framework**: Core Spotlight  
**Kind**: property

A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var supportsNavigation: NSNumber? { get set }
```

## Mentions

- [Adding your app’s content to Spotlight indexes](adding-your-app-s-content-to-spotlight-indexes.md)

#### Discussion

When an item includes [`latitude`](cssearchableitemattributeset/latitude.md) and [`longitude`](cssearchableitemattributeset/longitude.md) properties, these properties can be used for navigation to the location represented by the item. For example, it makes sense to set [`supportsNavigation`](cssearchableitemattributeset/supportsnavigation.md) to `1` for an item that represents review for a specific restaurant, but not for an item that represents a photo of a person.

## See Also

- [var actionIdentifiers: [String]](cssearchableitemattributeset/actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsPhoneCall: NSNumber?](cssearchableitemattributeset/supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [var sharedItemContentType: UTType?](cssearchableitemattributeset/shareditemcontenttype.md)
  The file type of the item to enable the user to share items from Spotlight.
- [let CSActionIdentifier: String](csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/supportsnavigation)*