# containerTitle

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The title of the container to which the item belongs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var containerTitle: String? { get set }
```

```objc
@property (copy, nullable) NSString * containerTitle;
```

## See Also

### Describing containment
- [var containerDisplayName: String?](./containerdisplayname.md)
  A localized string that specifies the name of a container to which the item belongs, suitable to display in the user interface.
- [var containerIdentifier: String?](./containeridentifier.md)
  The identifier of the container to which the item belongs.
- [var containerOrder: NSNumber?](./containerorder.md)
  The order of the item within the container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/containertitle)*