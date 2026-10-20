# present(completion:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method  
**Role**: Instance Method

Presents the payment sheet modally over your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func present(completion: (@Sendable (Bool) -> Void)? = nil)
```

```swift
func present() async -> Bool
```

```objc
- (void) presentWithCompletion:(void (^)(BOOL success)) completion;
```

#### Discussion

You are responsible for dismissing the payment sheet.

## Parameters

- `completion`: A block that is called after the sheet is presented. This block is passed the following parameters:

  - **success**: A Boolean value that indicates whether the payment sheet was successfully presented. [`true`](../../Swift/true.md) if the payment sheet was presented successfully; otherwise, [`false`](../../Swift/false.md).

## See Also

### Handling user interactions
- [var delegate: (any PKPaymentAuthorizationControllerDelegate)?](./delegate.md)
  The controller’s delegate.
- [protocol PKPaymentAuthorizationControllerDelegate](../pkpaymentauthorizationcontrollerdelegate.md)
  Methods that let you respond to user interactions with your payment authorization controller.
- [func dismiss(completion: (() -> Void)?)](./dismiss%28completion%29.md)
  Dismisses the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationcontroller/present(completion:))*