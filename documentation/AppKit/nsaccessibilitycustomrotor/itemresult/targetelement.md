# targetElement

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A target element that references an element to message for accessibility properties.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var targetElement: (any NSAccessibilityElementProtocol)? { get }
```

```objc
@property (weak, readonly, nullable) id<NSAccessibilityElement> targetElement;
```

## See Also

### Identifying an Item Result
- [var itemLoadingToken: NSAccessibilityLoadingToken?](./itemloadingtoken.md)
  A token to determine which item to return.
- [var targetRange: NSRange](./targetrange.md)
  A range that specifies the area of interest for text-based elements.
- [var customLabel: String?](./customlabel.md)
  A localized label to use instead of the default item label to describe the item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemresult/targetelement)*