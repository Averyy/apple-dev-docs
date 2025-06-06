# objc_cache

**Framework**: Objective-C Runtime

Performance optimization for method calls. Contains pointers to recently used methods.

#### Overview

To limit the need to perform linear searches of method lists for the definitions of frequently accessed methods—an operation that can considerably slow down method lookup—the Objective-C runtime functions store pointers to the definitions of the most recently called method of the class in an `objc_cache` data structure.

## Topics

### Fields
- [mask](1808499-mask.md)
  An integer specifying the total number of allocated cache buckets (minus one). During method lookup, the Objective-C runtime uses this field to determine the index at which to begin a linear search of the `buckets` array. A pointer to a method’s selector is masked against this field using a logical AND operation (`index = (mask & selector))`. This serves as a simple hashing algorithm.
- [occupied](1808501-occupied.md)
  An integer specifying the total number of occupied cache buckets.
- [buckets](1808503-buckets.md)
  An array of pointers to [`Method`](method.md) data structures. This array may contain no more than `mask + 1` items. Note that pointers may be `NULL`, indicating that the cache bucket is unoccupied, and occupied buckets may not be contiguous. This array may grow over time.

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
- [struct objc_property_attribute_t](objc_property_attribute_t.md)
  Defines a property attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_cache)*