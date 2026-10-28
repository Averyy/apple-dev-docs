# INObjectResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for an Object associated with an intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INObjectResolutionResult
```

```objc
@interface INObjectResolutionResult : INIntentResolutionResult
```

## Overview

An [`INObjectResolutionResult`](./inobjectresolutionresult.md) object is what you return when resolving Object related parameters of an intent object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INObject) -> Self](./inobjectresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INObject?) -> Self](./inobjectresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INObject]) -> Self](./inobjectresolutionresult/disambiguation%28with%29.md)
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

### Custom Resolution Results
- [class INEnumResolutionResult](./inenumresolutionresult.md)
  A resolution result for an enumeration associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inobjectresolutionresult)*