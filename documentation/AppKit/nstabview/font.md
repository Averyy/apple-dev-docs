# font

**Framework**: AppKit  
**Kind**: property

The font used for the tab view’s label text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var font: NSFont { get set }
```

#### Discussion

The default value of this property is the message font of default size (see [`messageFont(ofSize:)`](nsfont/messagefont(ofsize:).md)), which is equivalent to the system font of default size. Tab height is adjusted automatically to accommodate a new font size. If the view allows truncating, tab labels are truncated as needed.

## See Also

- [var allowsTruncatedLabels: Bool](nstabview/allowstruncatedlabels.md)
  A Boolean value that indicates if the tab view allows truncating for labels that don’t fit on a tab.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabview/font)*