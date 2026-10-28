# userCurated

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A value that indicates the user selected the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var userCurated: NSNumber? { get set }
```

```objc
@property (strong, getter=isUserCurated, nullable) NSNumber * userCurated;
```

## Discussion

Examples of items to set this property on include media content the user downloads and websites or news articles the user bookmarks.

## See Also

### Describing user involvement
- [var userCreated: NSNumber?](./usercreated.md)
  A value that indicates the user created the item.
- [var userOwned: NSNumber?](./userowned.md)
  A value that indicates the user purchased or owns the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/usercurated)*