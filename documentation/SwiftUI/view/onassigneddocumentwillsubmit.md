# onAssignedDocumentWillSubmit(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform before submitting an assigned document.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency func onAssignedDocumentWillSubmit(_ action: @escaping @Sendable (URL) async -> Bool) -> some View
```

#### Return Value

A view that executes the specified action before assigned document submission.

#### Discussion

Return `true` to allow the submission to proceed, or `false` to cancel the submission. This is useful for validating document content, confirming user intent, or performing prerequisite operations.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentWillSubmit { url in
        // Validate the assigned document before submission
        guard await isDocumentComplete(url) else {
            await showAlert("Please complete all sections before submitting")
            return false // Prevents submission
        }
        return true // Allows submission to continue
    }
```

## Parameters

- `action`: An asynchronous closure that receives the document URL and returns a Boolean value indicating whether to proceed with submission. Return `true` to continue, or `false` to cancel.

## See Also

- [func onAssignedDocumentDidSubmit((URL) -> Void) -> some View](view/onassigneddocumentdidsubmit(_:).md)
  Adds an action to perform after submitting an assigned document.
- [func onAssignedDocumentDidWithdraw((URL) -> Void) -> some View](view/onassigneddocumentdidwithdraw(_:).md)
  Adds an action to perform after an assigned document submission has been withdrawn.
- [func onAssignedDocumentWillWithdraw((URL) async -> Bool) -> some View](view/onassigneddocumentwillwithdraw(_:).md)
  Adds an action to perform before withdrawing an assigned document submission.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](view/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](view/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](view/submitlabel(_:).md)
  Sets the submit label for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillsubmit(_:))*