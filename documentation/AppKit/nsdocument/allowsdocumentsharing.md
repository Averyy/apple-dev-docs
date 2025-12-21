# allowsDocumentSharing

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the document is shareable from the standard Share menu.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
var allowsDocumentSharing: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the owning document controller enables share options for this document. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the document controller disables the Share menu when this document is selected.

## See Also

- [func prepare(NSSharingServicePicker)](nsdocument/prepare(_:).md)
  Perform any custom setup associated with a sharing service picker.
- [func share(with: NSSharingService, completionHandler: ((Bool) -> Void)?)](nsdocument/share(with:completionhandler:).md)
  Share the document’s file using the specified sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/allowsdocumentsharing)*