# prepare(_:)

**Framework**: AppKit  
**Kind**: method

Perform any custom setup associated with a sharing service picker.

**Availability**:
- macOS 10.13+

## Declaration

```swift
@MainActor
func prepare(_ sharingServicePicker: NSSharingServicePicker)
```

#### Discussion

Override this method, as needed, and use it to configure the sharing service picker before AppKit displays it. The default implementation of this method does nothing. You might customize the contents of the share menu or provide a custom delegate for the chosen sharing service. You can get the default sharing menu item by calling [`standardShareMenuItem()`](nsdocumentcontroller/standardsharemenuitem().md) on the current document controller.

## Parameters

- `sharingServicePicker`: The sharing service picker the system is about to display.

## See Also

- [var allowsDocumentSharing: Bool](nsdocument/allowsdocumentsharing.md)
  A Boolean value that indicates whether the document is shareable from the standard Share menu.
- [func share(with: NSSharingService, completionHandler: ((Bool) -> Void)?)](nsdocument/share(with:completionhandler:).md)
  Share the document’s file using the specified sharing service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/prepare(_:))*