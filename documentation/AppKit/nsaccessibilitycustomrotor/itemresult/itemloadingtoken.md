# itemLoadingToken

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A token to determine which item to return.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var itemLoadingToken: NSAccessibilityLoadingToken? { get }
```

```objc
@property (strong, readonly, nullable) NSAccessibilityLoadingToken itemLoadingToken;
```

## See Also

### Identifying an Item Result
- [var targetElement: (any NSAccessibilityElementProtocol)?](./targetelement.md)
  A target element that references an element to message for accessibility properties.
- [var targetRange: NSRange](./targetrange.md)
  A range that specifies the area of interest for text-based elements.
- [var customLabel: String?](./customlabel.md)
  A localized label to use instead of the default item label to describe the item result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitycustomrotor/itemresult/itemloadingtoken)*