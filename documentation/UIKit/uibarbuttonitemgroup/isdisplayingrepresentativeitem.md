# isDisplayingRepresentativeItem

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the representative item is showing in place of the group’s items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isDisplayingRepresentativeItem: Bool { get }
```

```objc
@property (nonatomic, assign, readonly, getter=isDisplayingRepresentativeItem) BOOL displayingRepresentativeItem;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the representative item is being displayed in the shortcuts bar. The value is [`false`](../../Swift/false.md) when the individual bar button items are being displayed in the shortcuts bar.

## See Also

### Determining the group’s appearance
- [var isHidden: Bool](./ishidden.md)
  A Boolean that determines the visibility of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/isdisplayingrepresentativeitem)*