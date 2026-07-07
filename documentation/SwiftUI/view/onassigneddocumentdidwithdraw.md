# onAssignedDocumentDidWithdraw(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform after an assigned document submission has been withdrawn.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency func onAssignedDocumentDidWithdraw(_ action: @escaping (URL) -> Void) -> some View
```

#### Return Value

A view that executes the specified action after submission withdrawal.

#### Discussion

This action runs regardless of whether you provided an [`onAssignedDocumentWillWithdraw(_:)`](view/onassigneddocumentwillwithdraw(_:).md) action, and only runs if the withdrawal completes successfully.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentDidWithdraw { url in
        // Handle successful withdrawal
        logEvent("Assigned document withdrawn successfully!")
    }
```

## Parameters

- `action`: An asynchronous closure that receives the document URL and executes after successful submission withdrawal.

## See Also

- [func onAssignedDocumentDidSubmit((URL) -> Void) -> some View](view/onassigneddocumentdidsubmit(_:).md)
  Adds an action to perform after submitting an assigned document.
- [func onAssignedDocumentWillSubmit((URL) async -> Bool) -> some View](view/onassigneddocumentwillsubmit(_:).md)
  Adds an action to perform before submitting an assigned document.
- [func onAssignedDocumentWillWithdraw((URL) async -> Bool) -> some View](view/onassigneddocumentwillwithdraw(_:).md)
  Adds an action to perform before withdrawing an assigned document submission.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](view/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](view/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](view/submitlabel(_:).md)
  Sets the submit label for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentdidwithdraw(_:))*