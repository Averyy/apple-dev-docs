# notRequired()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that you don’t need the value of the parameter.

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
class func notRequired() -> Self
```

```objc
+ (instancetype) notRequired;
```

#### Return Value

A new resolution result object.

#### Discussion

Use this method when you don’t need or use the value of a parameter to process an intent object. When you return a resolution object of this type, Siri ends the resolution process for the parameter.

## See Also

### Common Results
- [class func needsValue() -> Self](./needsvalue%28%29.md)
  Creates an object whose resolution indicates that a required parameter value is missing.
- [class func unsupported() -> Self](./unsupported%28%29.md)
  Creates an object whose resolution indicates that your app doesn’t support the specified value.
- [+ confirmationRequiredWithItemToConfirm:forReason:](./confirmationrequiredwithitemtoconfirm_forreason_.md)
  Creates an object whose resolution indicates that your app requires confirmation of the specified value.
- [+ unsupportedWithReason:](./unsupportedwithreason_.md)
  Creates an object whose resolution indicates that your app doesn’t support the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresolutionresult/notrequired())*