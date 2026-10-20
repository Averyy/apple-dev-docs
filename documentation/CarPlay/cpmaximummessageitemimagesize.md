# CPMaximumMessageItemImageSize

**Framework**: CarPlay  
**Kind**: var  
**Role**: Global Variable

The maximum size of a message list item’s image.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+

## Declaration

```swift
let CPMaximumMessageItemImageSize: CGSize
```

```c
extern const CGSize CPMaximumMessageItemImageSize;
```

#### Discussion

At runtime, use this value to determine the maximum size of an image that a message list item can display in its leading and trailing regions.

## See Also

### Creating a Configuration
- [init(leadingItem: CPMessageLeadingItem, leadingImage: UIImage?, unread: Bool)](./cpmessagelistitemleadingconfiguration/init%28leadingitem,leadingimage,unread%29.md)
  Creates a leading configuration that contains an item and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaximummessageitemimagesize)*