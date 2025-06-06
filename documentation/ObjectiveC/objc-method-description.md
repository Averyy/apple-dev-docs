# objc_method_description

**Framework**: Objective-C Runtime  
**Kind**: struct

Defines an Objective-C method.

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
struct objc_method_description
```

## Topics

### Fields
- [var name: Selector?](objc_method_description/name.md)
  The name of the method at runtime.
- [var types: UnsafeMutablePointer<CChar>?](objc_method_description/types.md)
  The types of the method arguments.
### Initializers
- [init()](objc_method_description/init.md)
- [init(name: Selector?, types: UnsafeMutablePointer<CChar>?)](objc_method_description/init(name:types:).md)

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
- [objc_cache](objc_cache.md)
  Performance optimization for method calls. Contains pointers to recently used methods.
- [struct objc_property_attribute_t](objc_property_attribute_t.md)
  Defines a property attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_method_description)*