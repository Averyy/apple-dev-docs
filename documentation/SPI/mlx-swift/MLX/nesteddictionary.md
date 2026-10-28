---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary"
framework: "mlx-swift/MLX"
---

# NestedDictionary

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Nested structure of arrays, dictionaries and values.

## Declaration

```swift
struct NestedDictionary<Key, Element> where Key : Hashable
```

## Overview

Some of the capabilities of `MLX` (especially in `MLXNN`) need to deal with arbitrarily structured values.  This is simple in python but swift needs type to describe the structure.

For example a nested dictionary / `[Int]` strucure might look like this:

```
[
  w1: [
    weight: [64, 20]
  ],
  w2: [
    weight: [20, 64]
  ]
]
```

This could be created with:

```swift
let contents: NestedItem<String, [Int]> =
    .dictionary([
        "w1": .dictionary([
            "weight": .value([64, 20])
        ]),
        "w2": .dictionary([
            "weight": .value([20, 64])
        ]),
    ])
let nd = NestedDictionary(item: contents)
```

In practice these structures are created programatically by traversing other nested structures.  The above example was actually created from code like this:

```swift
import MLXNN

class M : Module {
    let w1 = Linear(64, 20)
    let w2 = Linear(20, 64)
}

let nd = M().mapParameters { $0.shape }
```

### See Also

- [`NestedItem`](./nesteditem.md)

## Topics

### Initializers
- [init()](./nesteddictionary/init%28%29.md)
  Initialize an empty `NestedDictionary`.
- [init(item: NestedItem<Key, Element>)](./nesteddictionary/init%28item%29.md)
  Initialize with a [`NestedItem`](./nesteditem.md).
- [init(values: [Key : NestedItem<Key, Element>])](./nesteddictionary/init%28values%29.md)
  Initialize with a dictionary of [`NestedItem`](./nesteditem.md).
### Instance Properties
- [var count: Int](./nesteddictionary/count.md)
- [var description: String](./nesteddictionary/description.md)
- [var isEmpty: Bool](./nesteddictionary/isempty.md)
- [var keys: Dictionary<Key, NestedItem<Key, Element>>.Keys](./nesteddictionary/keys.md)
- [var values: Dictionary<Key, NestedItem<Key, Element>>.Values](./nesteddictionary/values.md)
### Instance Methods
- [func asDictionary() -> [Key : Any?]](./nesteddictionary/asdictionary%28%29.md)
- [func asItem() -> NestedItem<Key, Element>](./nesteddictionary/asitem%28%29.md)
- [func compactMapValues<Result>(transform: (Element) throws -> Result?) rethrows -> NestedDictionary<Key, Result>](./nesteddictionary/compactmapvalues%28transform%29.md)
  Transform the values in the nested structure using the `transform()` function.
- [func flattened(prefix: String?) -> [(String, Element)]](./nesteddictionary/flattened%28prefix%29.md)
  Return a flattened representation of the structured contents as an array of key/value tuples.
- [func flattenedValues() -> [Element]](./nesteddictionary/flattenedvalues%28%29.md)
  Return a flattened representation of the structured contents as an array of values.
- [func mapValues<E2, E3, R1, R2>(NestedDictionary<Key, E2>, NestedDictionary<Key, E3>, transform: (Element, E2?, E3?) -> (R1, R2?)) -> (NestedDictionary<Key, R1>, NestedDictionary<Key, R2>)](./nesteddictionary/mapvalues%28_,_,transform%29-52e9l.md)
  Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second and third `NestedDictionary`.
- [func mapValues<E2, E3, R1, R2, R3>(NestedDictionary<Key, E2>, NestedDictionary<Key, E3>, transform: (Element, E2?, E3?) throws -> (R1, R2?, R3?)) rethrows -> (NestedDictionary<Key, R1>, NestedDictionary<Key, R2>, NestedDictionary<Key, R3>)](./nesteddictionary/mapvalues%28_,_,transform%29-8yhzk.md)
  Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second and third `NestedDictionary`.
- [func mapValues<E2, R1>(NestedDictionary<Key, E2>, transform: (Element, E2?) -> R1) -> NestedDictionary<Key, R1>](./nesteddictionary/mapvalues%28_,transform%29-4ctis.md)
- [func mapValues<E2, R1, R2>(NestedDictionary<Key, E2>, transform: (Element, E2?) throws -> (R1, R2?)) rethrows -> (NestedDictionary<Key, R1>, NestedDictionary<Key, R2>)](./nesteddictionary/mapvalues%28_,transform%29-54sj2.md)
  Transform the values in the nested structure using the `transform()` function while simultaneously iterating the same structure in a second `NestedDictionary`.
- [func mapValues<Result>(transform: (Element) throws -> Result) rethrows -> NestedDictionary<Key, Result>](./nesteddictionary/mapvalues%28transform%29-1ehvq.md)
  Transform the values in the nested structure using the `transform()` function.
- [func mapValues<Result>(transform: (String, Element) throws -> Result) rethrows -> NestedDictionary<Key, Result>](./nesteddictionary/mapvalues%28transform%29-4q1m3.md)
  Transform the values in the nested structure using the `transform()` function.
- [func reduce<R>(R, (R, Element) throws -> R) rethrows -> R](./nesteddictionary/reduce%28_,_%29.md)
  Reduces the contents of the NestedDictionary by visiting each value and applying the `reducer` function, accumulating the result.
- [func replacingValues(with: some Collection<Element>) -> NestedDictionary<Key, Element>](./nesteddictionary/replacingvalues%28with%29.md)
  Return a new `NestedDictionary` with the values replaced by a flat array of values.
### Subscripts
- [subscript(Key) -> NestedItem<Key, Element>?](./nesteddictionary/subscript%28_%29-7bphj.md)
- [subscript(unwrapping _: Key) -> Element?](./nesteddictionary/subscript%28unwrapping%29.md)
### Type Aliases
- [NestedDictionary.CollectionElement](./nesteddictionary/collectionelement.md)
### Type Methods
- [static func unflattened([String : Element]) -> NestedDictionary<Key, Element>](./nesteddictionary/unflattened%28_%29-4p8bn.md)
  Convert a flattened dictionary back into a `NestedDictionary` structure.
- [static func unflattened(some Collection<(String, Element)>) -> NestedDictionary<Key, Element>](./nesteddictionary/unflattened%28_%29-7ubrp.md)
  Convert a flattened list of key/value tuples back into a `NestedDictionary` structure.
### Default Implementations
- [Collection Implementations](./nesteddictionary/collection-implementations.md)
- [Equatable Implementations](./nesteddictionary/equatable-implementations.md)
- [Sequence Implementations](./nesteddictionary/sequence-implementations.md)

## Relationships

### Conforms To
- Swift.Collection
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- Swift.Sequence

## See Also

### Nested Data
- [enum NestedItem](./nesteditem.md)
  Backing storage for [`NestedDictionary`](./nesteddictionary.md).
- [protocol IndentedDescription](./indenteddescription.md)
  Protocol for types that can provide an indented description, e.g. nested types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/nesteddictionary)*