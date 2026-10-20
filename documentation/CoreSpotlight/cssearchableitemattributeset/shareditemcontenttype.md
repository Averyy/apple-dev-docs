# sharedItemContentType

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The file type of the item to enable the user to share items from Spotlight.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var sharedItemContentType: UTType? { get set }
```

```objc
@property (copy, nullable) UTType * sharedItemContentType;
```

#### Discussion

Core Spotlight uses this property to determine the correct type identifier to pass to the [`fileURL(for:itemIdentifier:typeIdentifier:inPlace:)`](../cssearchableindexdelegate/fileurl%28for,itemidentifier,typeidentifier,inplace%29.md) method.

Spotlight enables sharing the item even if your app doesn’t set sharedItemContentType, but does support drag and drop for URL-backed types. Similarly, Spotlight enables copying items if your app supports drag and drop of Core Spotlight items.

## See Also

### Describing supporting actions
- [var actionIdentifiers: [String]](./actionidentifiers.md)
  The identifiers that specify custom actions the app supports for the item.
- [var supportsNavigation: NSNumber?](./supportsnavigation.md)
  A value that indicates whether the item contains information sufficient to provide navigation to the location it represents.
- [var supportsPhoneCall: NSNumber?](./supportsphonecall.md)
  A value that indicates whether the item contains information sufficient to allow a phone call to a number associated with the item.
- [let CSActionIdentifier: String](../csactionidentifier.md)
  A key that specifies the action’s identifier in a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/shareditemcontenttype)*