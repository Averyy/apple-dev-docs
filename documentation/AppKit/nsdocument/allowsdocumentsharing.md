# allowsDocumentSharing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the document is shareable from the standard Share menu.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var allowsDocumentSharing: Bool { get }
```

```objc
@property (readonly) BOOL allowsDocumentSharing;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the owning document controller enables share options for this document. When the value is [`false`](../../Swift/false.md), the document controller disables the Share menu when this document is selected.

## See Also

### Sharing the Document
- [func prepare(NSSharingServicePicker)](./prepare%28_%29.md)
  Perform any custom setup associated with a sharing service picker.
- [func share(with: NSSharingService, completionHandler: ((Bool) -> Void)?)](./share%28with,completionhandler%29.md)
  Share the document’s file using the specified sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/allowsdocumentsharing)*