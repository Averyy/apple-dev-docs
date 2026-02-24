# onAssignedDocumentWillWithdraw(_:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform before withdrawing an assigned document submission.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func onAssignedDocumentWillWithdraw(_ action: @escaping @Sendable (URL) async -> Bool) -> some View
```

#### Return Value

A view that executes the specified action before withdrawing an assigned document.

#### Discussion

Return `true` to allow the withdrawal to proceed or `false` to cancel it. This action confirms whether the person wants to withdraw their work.

```swift
AssignedDocumentSubmissionButton(documentURL: documentURL)
    .onAssignedDocumentWillWithdraw { url in
        // Confirm the person's intent
        let confirmed = await showConfirmation(
            "Are you sure you want to withdraw your document submission?"
        )
        return confirmed
    }
```

## Parameters

- `action`: An asynchronous closure that receives the document URL and returns a Boolean value indicating whether to proceed. Return `true` to continue, or `false` to cancel.

## See Also

- [func onAssignedDocumentDidSubmit((URL) -> Void) -> some View](view/onassigneddocumentdidsubmit(_:).md)
  Adds an action to perform after submitting an assigned document.
- [func onAssignedDocumentDidWithdraw((URL) -> Void) -> some View](view/onassigneddocumentdidwithdraw(_:).md)
  Adds an action to perform after an assigned document submission has been withdrawn.
- [func onAssignedDocumentWillSubmit((URL) async -> Bool) -> some View](view/onassigneddocumentwillsubmit(_:).md)
  Adds an action to perform before submitting an assigned document.
- [func onSubmit(of: SubmitTriggers, () -> Void) -> some View](view/onsubmit(of:_:).md)
  Adds an action to perform when the user submits a value to this view.
- [func submitScope(Bool) -> some View](view/submitscope(_:).md)
  Prevents submission triggers originating from this view to invoke a submission action configured by a submission modifier higher up in the view hierarchy.
- [func submitLabel(SubmitLabel) -> some View](view/submitlabel(_:).md)
  Sets the submit label for this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onassigneddocumentwillwithdraw(_:))*