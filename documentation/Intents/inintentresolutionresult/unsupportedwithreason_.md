# unsupportedWithReason:

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that your app doesn’t support the specified value.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
+ (instancetype) unsupportedWithReason:(NSInteger) reason;
```

## Return Value

A new `INIntentResolutionResult` object.

## Discussion

Use this method to create a resolution result object when your app doesn’t support an intent parameter. Siri may use the returned reason to let the user know that the value isn’t supported.

## Parameters

- `reason`: The reason why your app is not using the specified value. For a list of possible values, see `INIntentResolutionResultUnsupportedReason`.

## See Also

### Common Results
- [+ confirmationRequiredWithItemToConfirm:forReason:](./confirmationrequiredwithitemtoconfirm_forreason_.md)
  Creates an object whose resolution indicates that your app requires confirmation of the specified value.
- [class func needsValue() -> Self](./needsvalue%28%29.md)
  Creates an object whose resolution indicates that a required parameter value is missing.
- [class func notRequired() -> Self](./notrequired%28%29.md)
  Creates an object whose resolution indicates that you don’t need the value of the parameter.
- [class func unsupported() -> Self](./unsupported%28%29.md)
  Creates an object whose resolution indicates that your app doesn’t support the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresolutionresult/unsupportedwithreason:)*