# AssignedDocumentSubmissionButton

**Framework**: ClassKit UI  
**Kind**: struct

A button that provides submission functionality for the assigned document.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency struct AssignedDocumentSubmissionButton
```

#### Overview

`AssignedDocumentSubmissionButton` enables students to submit and withdraw assigned documents. The button fetches document data from ClassKit and updates its appearance and behavior based on the current submission status. The button shows loading states during both initial data loading and submission processing.

You can customize the submission process using view modifiers that execute at key points in the submission lifecycle. Use the modifiers to either validate or prepare documents before an action or update your app after an action completes:

For submissions, use:

- [`onAssignedDocumentWillSubmit(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onAssignedDocumentWillSubmit(_:)) to validate the document before submission.
- [`onAssignedDocumentDidSubmit(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onAssignedDocumentDidSubmit(_:)) to update your interface or log analytics after a successful submission.

For withdrawing submissions use:

- [`onAssignedDocumentWillWithdraw(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onAssignedDocumentWillWithdraw(_:)) to confirm the withdrawal action with the student or prepare your app state.
- [`onAssignedDocumentDidWithdraw(_:)`](https://developer.apple.com/documentation/SwiftUI/View/onAssignedDocumentDidWithdraw(_:)) to update your interface or notify the student that their document is no longer submitted.

The following example shows how to create an assigned document submission button and customize its behavior with validation and completion actions:

```swift
// Create a basic submission button
AssignedDocumentSubmissionButton(documentURL: documentURL)

// Create menu item with validation and logging
// Provide closures to validate document submissions and respond to completed submissions:
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentWillSubmit { url in
        // Validate the assigned document before submission
        guard await validateDocument(url) else {
            await showAlert("Please complete all sections before submitting")
            return false // Prevents submission
        }
        return true // Allows submission to continue
    }
    .onAssignedDocumentDidSubmit { url in
        // Handle successful submission
        logEvent("Assigned document submitted successfully!")
    }
```

## Topics

### Initializers
- [init(documentURL: URL)](assigneddocumentsubmissionbutton/init(documenturl:).md)
  Creates a button for document submission.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class AssignedDocumentDeferredMenuElement](assigneddocumentdeferredmenuelement.md)
  A deferred menu element that provides assigned document submission functionality.
- [class AssignedDocumentMenuItem](assigneddocumentmenuitem.md)
  A menu item that provides assigned document submission functionality.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitui/assigneddocumentsubmissionbutton)*