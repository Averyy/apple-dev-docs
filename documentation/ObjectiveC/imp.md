# IMP

**Framework**: Objective-C Runtime  
**Kind**: typealias

A pointer to the start of a method implementation.

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
typealias IMP = OpaquePointer
```

#### Discussion

This data type is a pointer to the start of the function that implements the method. This function uses standard C calling conventions as implemented for the current CPU architecture. The first argument is a pointer to `self` (that is, the memory for the particular instance of this class, or, for a class method, a pointer to the metaclass). The second argument is the method selector. The method arguments follow.

## See Also

- [typealias Method](method.md)
  An opaque type that represents a method in a class definition.
- [typealias Ivar](ivar.md)
  An opaque type that represents an instance variable.
- [typealias Category](category.md)
  An opaque type that represents a category.
- [typealias objc_property_t](objc_property_t.md)
  An opaque type that represents an Objective-C declared property.
- [struct objc_method_description](objc_method_description.md)
  Defines an Objective-C method.
- [objc_cache](objc_cache.md)
  Performance optimization for method calls. Contains pointers to recently used methods.
- [struct objc_property_attribute_t](objc_property_attribute_t.md)
  Defines a property attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/imp)*