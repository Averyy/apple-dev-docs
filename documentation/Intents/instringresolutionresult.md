# INStringResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for a string value associated with an intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INStringResolutionResult
```

```objc
@interface INStringResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INStringResolutionResult`](./instringresolutionresult.md) object is what you return when resolving parameters containing an [`NSString`](../Foundation/nsstring.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: String) -> Self](./instringresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: String?) -> Self](./instringresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [String]) -> Self](./instringresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Strings
- [class INSpeakableStringResolutionResult](./inspeakablestringresolutionresult.md)
  A resolution result for a speakable string object associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instringresolutionresult)*