# needsValue()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that a required parameter value is missing.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func needsValue() -> Self
```

```objc
+ (instancetype) needsValue;
```

#### Return Value

A new resolution result object.

#### Discussion

Use this method when a property of the intent object is missing a value that your app requires. When you return a resolution of this type, Siri prompts the user to provide the information and then passes the newly received value back to you for resolution. The cycle of prompting the user and asking you to resolve the parameter continues until you resolve the parameter successfully.

## See Also

### Common Results
- [class func notRequired() -> Self](./notrequired%28%29.md)
  Creates an object whose resolution indicates that you don’t need the value of the parameter.
- [class func unsupported() -> Self](./unsupported%28%29.md)
  Creates an object whose resolution indicates that your app doesn’t support the specified value.
- [+ confirmationRequiredWithItemToConfirm:forReason:](./confirmationrequiredwithitemtoconfirm_forreason_.md)
  Creates an object whose resolution indicates that your app requires confirmation of the specified value.
- [+ unsupportedWithReason:](./unsupportedwithreason_.md)
  Creates an object whose resolution indicates that your app doesn’t support the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresolutionresult/needsvalue())*