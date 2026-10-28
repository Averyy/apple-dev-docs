---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem"
framework: "mlx-swift/MLX"
---

# NestedItem

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Backing storage for [`NestedDictionary`](./nesteddictionary.md).

## Declaration

```swift
indirect enum NestedItem<Key, Element> where Key : Hashable
```

## Overview

`NestedItem` holds the array / dictionary / value structure contained in a `NestedDictionary`. Typically creation of these values is handled by code that returns `NestedDictionary` but these are used when traversing the structure manually.

### See Also

- [`NestedDictionary`](./nesteddictionary.md)
- [`mapValues(transform:)`](./nesteddictionary/mapvalues%28transform%29-1ehvq.md)
- [`mapValues(transform:)`](./nesteddictionary/mapvalues%28transform%29-1ehvq.md)
- [`flattened(prefix:)`](./nesteddictionary/flattened%28prefix%29.md)
- [`unflattened(_:)`](./nesteddictionary/unflattened%28_%29-4p8bn.md)

## Topics

### Enumeration Cases
- [case array([NestedItem<Key, Element>])](./nesteditem/array%28_%29.md)
- [case dictionary([Key : NestedItem<Key, Element>])](./nesteditem/dictionary%28_%29.md)
- [NestedItem.none](./nesteditem/none.md)
- [NestedItem.value(_:)](./nesteditem/value%28_%29.md)
### Instance Methods
- [func compactMapValues<Result>((Element) throws -> Result?) rethrows -> NestedItem<Key, Result>](./nesteditem/compactmapvalues%28_%29.md)
  Transform the values in the nested structure using the `transform()` function.
- [func description(indent: Int) -> String](./nesteditem/description%28indent%29.md)
  Return the `description` with the given indent level.
- [func flattened(prefix: String?) -> [(String, Element)]](./nesteditem/flattened%28prefix%29.md)
  Return a flattened representation of the structured contents as an array of key/value tuples.
- [func flattenedValues() -> [Element]](./nesteditem/flattenedvalues%28%29.md)
  Return a flattened representation of the structured contents as an array of values.
- [func mapValues<Result>((Element) throws -> Result) rethrows -> NestedItem<Key, Result>](./nesteditem/mapvalues%28_%29.md)
  Transform the values in the nested structure using the `transform()` function.
- [func mapValues<E2, R1, R2>(NestedItem<Key, E2>, (Element, E2?) throws -> (R1, R2?)) rethrows -> (NestedItem<Key, R1>, NestedItem<Key, R2>)](./nesteditem/mapvalues%28_,_%29.md)
  Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second `NestedItem`.
- [func mapValues<E2, E3, R1, R2, R3>(NestedItem<Key, E2>, NestedItem<Key, E3>, (Element, E2?, E3?) throws -> (R1, R2?, R3?)) rethrows -> (NestedItem<Key, R1>, NestedItem<Key, R2>, NestedItem<Key, R3>)](./nesteditem/mapvalues%28_,_,_%29.md)
  Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second and third `NestedItem`.
- [func mapValues<Result>(prefix: String?, (String, Element) throws -> Result) rethrows -> NestedItem<Key, Result>](./nesteditem/mapvalues%28prefix,_%29.md)
  A combination of [`mapValues(_:)`](./nesteditem/mapvalues%28_%29.md), [`flattened(prefix:)`](./nesteditem/flattened%28prefix%29.md) and [`unflattened(_:)`](./nesteditem/unflattened%28_%29.md).
- [func reduce<R>(R, (R, Element) throws -> R) rethrows -> R](./nesteditem/reduce%28_,_%29.md)
  Reduces the contents of the NestedDictionary by visiting each value and applying the `reducer` function, accumulating the result.
- [func unwrap() -> Any?](./nesteditem/unwrap%28%29.md)
  Return the values contained inside as a type erased swift structure, e.g. normal `Array` and `Dictionary`. This is suitable for tests and debugging but should not be used in typical code.
### Type Methods
- [static func unflattened(some Collection<(String, Element)>) -> NestedItem<Key, Element>](./nesteditem/unflattened%28_%29.md)
  Convert a flattened list of key/value tuples back into a `NestedItem` structure.
### Default Implementations
- [CustomStringConvertible Implementations](./nesteditem/customstringconvertible-implementations.md)
- [Equatable Implementations](./nesteditem/equatable-implementations.md)

## Relationships

### Conforms To
- [IndentedDescription](./indenteddescription.md)
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Nested Data
- [struct NestedDictionary](./nesteddictionary.md)
  Nested structure of arrays, dictionaries and values.
- [protocol IndentedDescription](./indenteddescription.md)
  Protocol for types that can provide an indented description, e.g. nested types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteditem)*