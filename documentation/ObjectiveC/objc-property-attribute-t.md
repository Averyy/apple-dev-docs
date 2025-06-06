# objc_property_attribute_t

**Framework**: Objective-C Runtime  
**Kind**: struct

Defines a property attribute.

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
struct objc_property_attribute_t
```

## Topics

### Initializers
- [init(name: UnsafePointer<CChar>, value: UnsafePointer<CChar>)](objc_property_attribute_t/init(name:value:).md)
### Instance Properties
- [var name: UnsafePointer<CChar>](objc_property_attribute_t/name.md)
  The name of the attribute.
- [var value: UnsafePointer<CChar>](objc_property_attribute_t/value.md)
  The value of the attribute (usually empty).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias Method](method.md)
  An opaque type that represents a method in a class definition.
- [typealias Ivar](ivar.md)
  An opaque type that represents an instance variable.
- [typealias Category](category.md)
  An opaque type that represents a category.
- [typealias objc_property_t](objc_property_t.md)
  An opaque type that represents an Objective-C declared property.
- [typealias IMP](imp.md)
  A pointer to the start of a method implementation.
- [struct objc_method_description](objc_method_description.md)
  Defines an Objective-C method.
- [objc_cache](objc_cache.md)
  Performance optimization for method calls. Contains pointers to recently used methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_property_attribute_t)*