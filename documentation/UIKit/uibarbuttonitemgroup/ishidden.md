# isHidden

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that determines the visibility of the group.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var isHidden: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite, getter=isHidden) BOOL hidden;
```

#### Discussion

Set this property to [`true`](../../Swift/true.md) to hide the group, or [`false`](../../Swift/false.md) to display the group.

## See Also

### Determining the group’s appearance
- [var isDisplayingRepresentativeItem: Bool](./isdisplayingrepresentativeitem.md)
  A Boolean value indicating whether the representative item is showing in place of the group’s items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/ishidden)*