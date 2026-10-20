# userOwned

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A value that indicates the user purchased or owns the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var userOwned: NSNumber? { get set }
```

```objc
@property (strong, getter=isUserOwned, nullable) NSNumber * userOwned;
```

#### Discussion

Examples of items to set this property on include songs and movies the user purchases.

## See Also

### Describing user involvement
- [var userCreated: NSNumber?](./usercreated.md)
  A value that indicates the user created the item.
- [var userCurated: NSNumber?](./usercurated.md)
  A value that indicates the user selected the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/userowned)*