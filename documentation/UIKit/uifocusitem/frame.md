# frame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The geometric frame of the item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var frame: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect frame;
```

#### Discussion

The item’s frame must be expressed in the coordinate space of the [`UIFocusItemContainer`](../uifocusitemcontainer.md) that contains it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusitem/frame)*