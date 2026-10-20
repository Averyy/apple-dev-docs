# validateCaptionConversion(warningHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Validates the object’s captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
func validateCaptionConversion(warningHandler handler: @escaping @Sendable (AVCaptionConversionWarning?) -> Void)
```

```objc
- (void) validateCaptionConversionWithWarningHandler:(void (^)(AVCaptionConversionWarning *warning)) handler;
```

#### Discussion

When the object finishes validating and reports all warnings, it invokes the callback once with a value of `nil` for its warning parameter. When this occurs, the validator’s [`status`](./status-swift.property.md) value changes to [`AVCaptionConversionValidator.Status.completed`](./status-swift.enum/completed.md).

Stop an in-progress validation operation by calling [`stopValidating()`](./stopvalidating%28%29.md).

> ❗ **Important**:  It’s only valid to call this method when the validator’s state is [`AVCaptionConversionValidator.Status.unknown`](./status-swift.enum/unknown.md).

## Parameters

- `handler`: The callback the system invokes when it finishes validation.

## See Also

### Validating captions
- [var warnings: [AVCaptionConversionWarning]](./warnings.md)
  The collection of warnings the validator encountered.
- [class AVCaptionConversionWarning](../avcaptionconversionwarning.md)
  An object that represents a conversion warning produced by a validator.
- [func stopValidating()](./stopvalidating%28%29.md)
  Stops the active validation operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptionconversionvalidator/validatecaptionconversion(warninghandler:))*