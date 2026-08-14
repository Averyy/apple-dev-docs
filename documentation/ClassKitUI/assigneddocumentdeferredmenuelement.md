# AssignedDocumentDeferredMenuElement

**Framework**: ClassKit UI  
**Kind**: class

A deferred menu element that provides assigned document submission functionality.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@objc @preconcurrency class AssignedDocumentDeferredMenuElement
```

#### Overview

`AssignedDocumentDeferredMenuElement` enables students to submit and withdraw assigned documents directly from UIKit menus. The menu element loads asynchronously, fetching document metadata from ClassKit and displaying the appropriate action based on the current submission status. The element shows an in-line spinner during both initial loading and submission processing.

The following example shows how to create an assigned document menu item and customize its behavior with validation and completion actions:

```swift
// Create a basic assigned document submission menu element
let menuElement = AssignedDocumentDeferredMenuElement(documentURL: documentURL)
menu.children = [menuElement]

// Create menu item with validation and logging
let menuElement = AssignedDocumentDeferredMenuElement(
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
- [convenience init(documentURL: URL, willSubmit: (URL) async -> Bool, didSubmit: (URL) -> Void, willWithdraw: (URL) async -> Bool, didWithdraw: (URL) -> Void)](assigneddocumentdeferredmenuelement/init(documenturl:willsubmit:didsubmit:willwithdraw:didwithdraw:).md)
  Creates a deferred menu element for assigned document submissions.

## Relationships

### Inherits From
- [UIDeferredMenuElement](../uikit/uideferredmenuelement.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)

## See Also

- [struct AssignedDocumentSubmissionButton](assigneddocumentsubmissionbutton.md)
  A button that provides submission functionality for the assigned document.
- [class AssignedDocumentMenuItem](assigneddocumentmenuitem.md)
  A menu item that provides assigned document submission functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitui/assigneddocumentdeferredmenuelement)*