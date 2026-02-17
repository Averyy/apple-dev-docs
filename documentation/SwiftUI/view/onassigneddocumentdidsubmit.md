# onAssignedDocumentDidSubmit(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform after submitting an assigned document.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func onAssignedDocumentDidSubmit(_ action: @escaping (URL) -> Void) -> some View
```

#### Return Value

A view that executes the specified action after assigned document submission.

#### Discussion

This action runs only after successful submission, regardless of whether you provided an [`onAssignedDocumentWillSubmit(_:)`](view/onassigneddocumentwillsubmit(_:).md) action.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentDidSubmit { url in
        // Handle successful submission
        logEvent("Assigned document submitted successfully!")
    }
```

## Parameters

- `action`: An asynchronous closure that receives the document URL and   executes after successful submission.

## See Also

- [func onAssignedDocumentDidWithdraw((URL) -> Void) -> some View](view/onassigneddocumentdidwithdraw(_:).md)
  Adds an action to perform after an assigned document submission has been withdrawn.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentdidsubmit(_:))*