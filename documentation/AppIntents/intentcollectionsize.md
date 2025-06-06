# IntentCollectionSize

**Framework**: App Intents  
**Kind**: struct

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct IntentCollectionSize
```

## Topics

### Operators
- [static func == (IntentCollectionSize, IntentCollectionSize) -> Bool](intentcollectionsize/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(exactly: Int)](intentcollectionsize/init(exactly:).md)
- [init(integerLiteral: Int)](intentcollectionsize/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(min: Int, max: Int)](intentcollectionsize/init(min:max:).md)
### Type Aliases
- [IntentCollectionSize.IntegerLiteralType](intentcollectionsize/integerliteraltype.md)
  A type that represents an integer literal.
### Default Implementations
- [Equatable Implementations](intentcollectionsize/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)

## See Also

- [struct IntentItem](intentitem.md)
  A type describing a value returned from a dynamic options provider, plus information about how to display it to users.
- [struct IntentItemCollection](intentitemcollection.md)
  Return this object to provide an advanced list of options, optionally divided in sections.
- [struct IntentItemSection](intentitemsection.md)
  An object you use to divide dynamic options into sections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentcollectionsize)*