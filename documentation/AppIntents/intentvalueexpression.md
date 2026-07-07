# IntentValueExpression

**Framework**: App Intents  
**Kind**: struct

A type that represents a lazily evaluated intent value.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct IntentValueExpression
```

#### Overview

`IntentValueExpression` provides a mechanism for lazy evaluation of intent values, allowing values to be converted to containers only when needed. This approach improves performance by deferring potentially expensive conversions until they’re actually required.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol IntentValueQuery](intentvaluequery.md)
  A query that provides entity values to the system; for example, for visual intelligence search.
- [struct IntentValueContainer](intentvaluecontainer.md)
  A container that stores a value that supports intent value conversion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvalueexpression)*