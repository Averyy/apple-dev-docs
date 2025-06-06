# printInfo

**Framework**: AppKit  
**Kind**: property

The printing information object used when the page layout panel is run.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var printInfo: NSPrintInfo? { get }
```

#### Discussion

The NSPrintInfo object is set using the [`beginSheet(with:modalFor:delegate:didEnd:contextInfo:)`](nspagelayout/beginsheet(with:modalfor:delegate:didend:contextinfo:).md) or [`runModal(with:)`](nspagelayout/runmodal(with:).md) method. The shared NSPrintInfo object is used if the receiver is run using [`runModal()`](nspagelayout/runmodal().md).

## See Also

- [class NSPrintInfo](nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPageLayout.Result](nspagelayout/result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/printinfo)*