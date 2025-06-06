# objc_super

**Framework**: Objective-C Runtime  
**Kind**: struct

Specifies the superclass of an instance.

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
struct objc_super
```

#### Discussion

The compiler generates an `objc_super` data structure when it encounters the `super` keyword as the receiver of a message. It specifies the class definition of the particular superclass that should be messaged.

## Topics

### Fields
- [var receiver: Unmanaged<AnyObject>](objc_super-swift.struct/receiver.md)
  A pointer of type [`objc_object`](objc_object.md). Specifies an instance of a class.
- [var super_class: AnyClass](objc_super-swift.struct/super_class.md)
  A pointer to a [`Class`](class.md) data structure. Specifies the particular superclass of the instance to message.
### Instance Properties
- [var receiver: Unmanaged<AnyObject>](objc_super-swift.struct/receiver.md)
  A pointer of type [`objc_object`](objc_object.md). Specifies an instance of a class.
- [var super_class: AnyClass](objc_super-swift.struct/super_class.md)
  A pointer to a [`Class`](class.md) data structure. Specifies the particular superclass of the instance to message.
### Initializers
- [init(receiver: Unmanaged<AnyObject>, super_class: AnyClass)](objc_super-swift.struct/init(receiver:super_class:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct objc_object](objc_object.md)
  Represents an instance of a class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_super-swift.struct)*