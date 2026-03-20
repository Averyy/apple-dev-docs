# init(documentURL:willSubmit:didSubmit:willWithdraw:didWithdraw:)

**Framework**: ClassKit UI  
**Kind**: init

Creates a deferred menu element for assigned document submissions.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- visionOS 26.4+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(documentURL: URL, willSubmit: @escaping @Sendable (URL) async -> Bool = { _ in true }, didSubmit: @escaping (URL) -> Void = { _ in }, willWithdraw: @escaping @Sendable (URL) async -> Bool = { _ in true }, didWithdraw: @escaping (URL) -> Void = { _ in })
```

## Parameters

- `documentURL`: The URL of the assigned document.
- `willSubmit`: A closure that executes before submission. Return `false` to prevent submission.
- `didSubmit`: A closure that executes after successful submission.
- `willWithdraw`: A closure that executes before withdrawing. Return `false` to prevent withdrawal.
- `didWithdraw`: A closure that executes after successful withdrawal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitui/assigneddocumentdeferredmenuelement/init(documenturl:willsubmit:didsubmit:willwithdraw:didwithdraw:))*