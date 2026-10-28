# allowsTruncatedLabels

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the tab view allows truncating for labels that don’t fit on a tab.

**Availability**:
- macOS

## Declaration

```swift
var allowsTruncatedLabels: Bool { get set }
```

```objc
@property BOOL allowsTruncatedLabels;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the tab view allows truncating for labels that don’t fit on a tab, otherwise it does not. The default value is [`true`](../../Swift/true.md). When truncating is allowed, the tab view inserts an ellipsis, if necessary, to fit a label in the tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/allowstruncatedlabels)*