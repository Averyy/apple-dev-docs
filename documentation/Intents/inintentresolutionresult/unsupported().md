# unsupported()

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that your app doesn’t support the specified value.

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
class func unsupported() -> Self
```

```objc
+ (instancetype) unsupported;
```

#### Return Value

A new resolution result object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support an intent parameter. When you return a resolution of this type, Siri prompts the user to provide a new value and then passes that value back to you for resolution. The cycle of prompting the user and asking you to resolve the parameter continues until you resolve the parameter successfully.

## See Also

### Common Results
- [class func needsValue() -> Self](./needsvalue%28%29.md)
  Creates an object whose resolution indicates that a required parameter value is missing.
- [class func notRequired() -> Self](./notrequired%28%29.md)
  Creates an object whose resolution indicates that you don’t need the value of the parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inintentresolutionresult/unsupported())*