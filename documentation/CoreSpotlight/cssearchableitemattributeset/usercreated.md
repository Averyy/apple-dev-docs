# userCreated

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A value that indicates the user created the item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+

## Declaration

```swift
var userCreated: NSNumber? { get set }
```

```objc
@property (strong, getter=isUserCreated, nullable) NSNumber * userCreated;
```

## Discussion

Examples of items to set this property on include notes and documents that the user creates or modifies.

## See Also

### Describing user involvement
- [var userCurated: NSNumber?](./usercurated.md)
  A value that indicates the user selected the item.
- [var userOwned: NSNumber?](./userowned.md)
  A value that indicates the user purchased or owns the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/usercreated)*