# containerIdentifier

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

The identifier of the container to which the item belongs.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var containerIdentifier: String? { get set }
```

```objc
@property (copy, nullable) NSString * containerIdentifier;
```

## See Also

### Describing containment
- [var containerDisplayName: String?](./containerdisplayname.md)
  A localized string that specifies the name of a container to which the item belongs, suitable to display in the user interface.
- [var containerOrder: NSNumber?](./containerorder.md)
  The order of the item within the container.
- [var containerTitle: String?](./containertitle.md)
  The title of the container to which the item belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/containeridentifier)*