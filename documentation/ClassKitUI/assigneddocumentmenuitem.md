# AssignedDocumentMenuItem

**Framework**: ClassKit UI  
**Kind**: class  
**Role**: Class

A menu item that provides assigned document submission functionality.

**Availability**:
- macOS 26.4+

## Declaration

```swift
@objc
class AssignedDocumentMenuItem
```

#### Overview

`AssignedDocumentMenuItem` enables students to submit and withdraw assigned documents directly from AppKit menus. The menu element loads asynchronously, fetching document metadata from ClassKit and displaying the appropriate action based on the current submission status. The element shows an in-line spinner during both initial loading and submission processing.

The following example shows how to create an assigned document menu item and customize its behavior with validation and completion actions:

```swift
let menuItem = AssignedDocumentMenuItem(
    documentURL: documentURL,
    willSubmit: { url in
        // Validate the assigned document before submission
        guard await validateDocument(url) else {
            await showAlert("Please complete all sections before submitting")
            return false // Prevents submission
        }
        return true // Allows submission to continue
    },
    didSubmit: { url in
        // Handle successful submission
        logEvent("Assigned document submitted successfully!")
    }
)
// Add the configured item to the menu
menu.addItem(menuItem)
```

## Topics

### Initializers
- [init(documentURL: URL, willSubmit: (URL) async -> Bool, didSubmit: (URL) -> Void, willWithdraw: (URL) async -> Bool, didWithdraw: (URL) -> Void)](./assigneddocumentmenuitem/init%28documenturl,willsubmit,didsubmit,willwithdraw,didwithdraw%29.md)
  Creates a menu item for assigned document submission.

## Relationships

### Inherits From
- [NSMenuItem](../AppKit/nsmenuitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSValidatedUserInterfaceItem](../AppKit/nsvalidateduserinterfaceitem.md)

## See Also

### Submitting assigned documents
- [struct AssignedDocumentSubmissionButton](./assigneddocumentsubmissionbutton.md)
  A button that provides submission functionality for the assigned document.
- [class AssignedDocumentDeferredMenuElement](./assigneddocumentdeferredmenuelement.md)
  A deferred menu element that provides assigned document submission functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitui/assigneddocumentmenuitem)*