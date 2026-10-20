# printInfo

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The printing information object used when the page layout panel is run.

**Availability**:
- macOS

## Declaration

```swift
var printInfo: NSPrintInfo? { get }
```

```objc
@property (strong, readonly, nullable) NSPrintInfo * printInfo;
```

#### Discussion

The NSPrintInfo object is set using the [`beginSheet(with:modalFor:delegate:didEnd:contextInfo:)`](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md) or [`runModal(with:)`](./runmodal%28with%29.md) method. The shared NSPrintInfo object is used if the receiver is run using [`runModal()`](./runmodal%28%29.md).

## See Also

### Accessing the printing information
- [class NSPrintInfo](../nsprintinfo.md)
  An object that stores information that’s used to generate printed output.
- [NSPageLayout.Result](./result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagelayout/printinfo)*