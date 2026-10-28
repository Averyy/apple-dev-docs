# resolveVisualCodeType(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the type of code requested by the user.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
optional func resolveVisualCodeType(for intent: INGetVisualCodeIntent, with completion: @escaping @Sendable (INVisualCodeTypeResolutionResult) -> Void)
```

```swift
optional func resolveVisualCodeType(for intent: INGetVisualCodeIntent) async -> INVisualCodeTypeResolutionResult
```

```objc
- (void) resolveVisualCodeTypeForGetVisualCode:(INGetVisualCodeIntent *) intent withCompletion:(void (^)(INVisualCodeTypeResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify that your app supports providing a code of the specified type. If your app supports the requested code or supports only one type of code, return a resolution of success with the code type that you support. If your app doesn’t support the requested type of visual code, provide a resolution asking the user to confirm the code type that you do support.

## Parameters

- `intent`: The intent object containing details of the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution object containing your proposed resolution. For successful resolutions, create a resolution object whose value is the [`INVisualCodeType`](../invisualcodetype.md) value representing the requested code type. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintenthandling/resolvevisualcodetype(for:with:))*