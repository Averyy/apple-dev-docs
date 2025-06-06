# isDisplayingRepresentativeItem

**Framework**: UIKit  
**Kind**: property

A Boolean value indicating whether the representative item is showing in place of the group’s items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isDisplayingRepresentativeItem: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the representative item is being displayed in the shortcuts bar. The value is [`false`](https://developer.apple.com/documentation/swift/false) when the individual bar button items are being displayed in the shortcuts bar.

## See Also

- [var isHidden: Bool](uibarbuttonitemgroup/ishidden.md)
  A Boolean that determines the visibility of the group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibarbuttonitemgroup/isdisplayingrepresentativeitem)*