# INEnumResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for an enumeration associated with an intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INEnumResolutionResult
```

```objc
@interface INEnumResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INEnumResolutionResult`](./inenumresolutionresult.md) object is what you return when resolving enumeration related parameters of an intent object. Use the creation method that best reflects your ability to successfully resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

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
- [class INObjectResolutionResult](./inobjectresolutionresult.md)
  A resolution result for an Object associated with an intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inenumresolutionresult)*