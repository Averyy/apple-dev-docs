# CombineIdentifier

**Framework**: Combine  
**Kind**: struct

A unique identifier for identifying publisher streams.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct CombineIdentifier
```

#### Overview

To conform to [`CustomCombineIdentifierConvertible`](customcombineidentifierconvertible.md) in a [`Subscription`](subscription.md) or [`Subject`](subject.md) that you implement as a structure, create an instance of [`CombineIdentifier`](combineidentifier.md) as follows:

```swift
let combineIdentifier = CombineIdentifier()
```

## Topics

### Creating a Combine identifier
- [init()](combineidentifier/init.md)
  Creates a unique Combine identifier.
- [init(AnyObject)](combineidentifier/init(_:).md)
  Creates a Combine identifier, using the bit pattern of the provided object.
### Providing a description
- [var description: String](combineidentifier/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol CustomCombineIdentifierConvertible](customcombineidentifierconvertible.md)
  A protocol for uniquely identifying publisher streams.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/combineidentifier)*