# containerOrder

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The order of the item within the container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var containerOrder: NSNumber? { get set }
```

```objc
@property (strong, nullable) NSNumber * containerOrder;
```

## Discussion

For example, if the container represents a series of books, this property specifies the order in which the books should be read.

## See Also

### Describing containment
- [var containerDisplayName: String?](./containerdisplayname.md)
  A localized string that specifies the name of a container to which the item belongs, suitable to display in the user interface.
- [var containerIdentifier: String?](./containeridentifier.md)
  The identifier of the container to which the item belongs.
- [var containerTitle: String?](./containertitle.md)
  The title of the container to which the item belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/containerorder)*