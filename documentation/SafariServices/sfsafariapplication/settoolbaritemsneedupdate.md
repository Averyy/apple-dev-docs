# setToolbarItemsNeedUpdate()

**Framework**: Safari Services  
**Kind**: method

Updates the enabled states and badges of toolbar items.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class func setToolbarItemsNeedUpdate()
```

#### Discussion

This method calls the [`validateToolbarItem(in:validationHandler:)`](sfsafariextensionhandling/validatetoolbaritem(in:validationhandler:).md) method on the extension’s principal object for each open window. See [`SFSafariExtensionHandling`](sfsafariextensionhandling.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariapplication/settoolbaritemsneedupdate())*