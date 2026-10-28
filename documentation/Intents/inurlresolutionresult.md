# INURLResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the types media destinations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INURLResolutionResult
```

```objc
@interface INURLResolutionResult : INIntentResolutionResult
```

## Overview

You return an [`INURLResolutionResult`](./inurlresolutionresult.md) object when resolving parameters containing an [`NSURL`](../Foundation/nsurl.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [class func success(with: URL) -> Self](./inurlresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: URL?) -> Self](./inurlresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [URL]) -> Self](./inurlresolutionresult/disambiguation%28with%29.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inurlresolutionresult)*