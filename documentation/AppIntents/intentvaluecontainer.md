# IntentValueContainer

**Framework**: App Intents  
**Kind**: struct

A container that stores a value that supports intent value conversion.

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
struct IntentValueContainer
```

#### Overview

The `IntentValueContainer` structure provides a type-erased wrapper around values that the App Intents framework can use. It encapsulates the actual value as a container element and provides mechanisms for type-safe access and conversion.

This container serves as an intermediate representation when converting between different types.

## Topics

### Structures
- [IntentValueContainer.ConversionContext](intentvaluecontainer/conversioncontext.md)
  A context that provides additional information for value conversion.
### Operators
- [static func == (IntentValueContainer, IntentValueContainer) -> Bool](intentvaluecontainer/==(_:_:).md)
  Returns a Boolean value indicating whether two containers are equal.
### Default Implementations
- [IntentValueExpressing Implementations](intentvaluecontainer/intentvalueexpressing-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [IntentValueExpressing](intentvalueexpressing.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [protocol IntentValueQuery](intentvaluequery.md)
  A query that provides entity values to the system; for example, for visual intelligence search.
- [struct IntentValueExpression](intentvalueexpression.md)
  A type that represents a lazily evaluated intent value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentvaluecontainer)*