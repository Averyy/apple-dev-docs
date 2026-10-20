# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that reflects whether or not the item is visible.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.12.2+

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (readonly, getter=isVisible) BOOL visible;
```

#### Discussion

When [`true`](../../Swift/true.md), this item is shown in a currently visible bar. This property is always [`false`](../../Swift/false.md) for spaces, proxy items, and groups.

This property is key-value observable.

## See Also

### Managing item visibility
- [var visibilityPriority: NSTouchBarItem.Priority](./visibilitypriority.md)
  Determines which items are shown in a bar when space is limited.
- [NSTouchBarItem.Priority](./priority.md)
  Priorities for the visibility of a Touch Bar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstouchbaritem/isvisible)*