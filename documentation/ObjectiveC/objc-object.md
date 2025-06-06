# objc_object

**Framework**: Objective-C Runtime  
**Kind**: struct

Represents an instance of a class.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct objc_object
```

## Topics

### Initializers
- [init(isa: AnyClass)](objc_object/init(isa:).md)
### Instance Properties
- [var isa: AnyClass](objc_object/isa.md)
  A pointer to the class definition of which this object is an instance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct objc_super](objc_super-swift.struct.md)
  Specifies the superclass of an instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_object)*