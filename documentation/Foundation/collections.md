# Collections

**Framework**: Foundation

Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.

## Topics

### Basic Collections
- [@frozen struct Array<Element>](../Swift/Array.md)
  An ordered, random-access collection.
- [@frozen struct Dictionary<Key, Value> where Key : Hashable](../Swift/Dictionary.md)
  A collection whose elements are key-value pairs.
- [@frozen struct Set<Element> where Element : Hashable](../Swift/Set.md)
  An unordered collection of unique elements.
### Indexes
- [struct IndexPath](indexpath.md)
  A list of indexes that together represent the path to a specific location in a tree of nested arrays.
- [struct IndexSet](indexset.md)
  A collection of unique integer values that represent the indexes of elements in another collection.
### Specialized Sets
- [class NSCountedSet](nscountedset.md)
  A mutable, unordered collection of distinct objects that may appear more than once in the collection.
- [class NSOrderedSet](nsorderedset.md)
  A static, ordered collection of unique objects.
- [class NSMutableOrderedSet](nsmutableorderedset.md)
  A dynamic, ordered collection of unique objects.
### Purgeable Collections
- [class NSCache](nscache.md)
  A mutable collection you use to temporarily store transient key-value pairs that are subject to eviction when resources are low.
- [class NSPurgeableData](nspurgeabledata.md)
  A mutable data object containing bytes that can be discarded when they’re no longer needed.
### Pointer Collections
- [class NSPointerArray](nspointerarray.md)
  A collection similar to an array, but with a broader range of available memory semantics.
- [class NSMapTable](nsmaptable.md)
  A collection similar to a dictionary, but with a broader range of available memory semantics.
- [class NSHashTable](nshashtable.md)
  A collection similar to a set, but with broader range of available memory semantics.
### Iteration
- [class NSEnumerator](nsenumerator.md)
  An abstract class whose subclasses enumerate collections of objects, such as arrays and dictionaries.
- [protocol NSFastEnumeration](nsfastenumeration.md)
  A protocol that objects adopt to support fast enumeration.
- [struct NSFastEnumerationIterator](nsfastenumerationiterator.md)
- [struct NSIndexSetIterator](nsindexsetiterator.md)
  An iterator suitable for enumerating the elements of an index set.
- [struct NSEnumerationOptions](nsenumerationoptions.md)
  Options for block enumeration operations.
- [struct NSSortOptions](nssortoptions.md)
  Options for block sorting operations.
### Special Semantic Values
- [class NSNull](nsnull.md)
  A singleton object used to represent null values in collection objects that don’t allow `nil` values.
- [let NSNotFound: Int](nsnotfound-9t5v2.md)
- [let NSNotFound: Int](nsnotfound-4qp9h.md)
  A value indicating that a requested item couldn’t be found or doesn’t exist.

## See Also

- [Numbers, Data, and Basic Values](numbers-data-and-basic-values.md)
  Work with primitive values and other fundamental types used throughout Cocoa.
- [Strings and Text](strings-and-text.md)
  Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Dates and Times](dates-and-times.md)
  Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md)
  Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md)
  Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md)
  Use predicates, expressions, and sort descriptors to examine elements in collections and other services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/collections)*