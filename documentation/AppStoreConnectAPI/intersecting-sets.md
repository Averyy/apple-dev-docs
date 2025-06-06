# Intersecting sets

**Framework**: App Store Connect API

Return the intersection of two or more arrays treated as sets.

#### Overview

Use the `intersection()` function in the expression of a matchmaking rule to find the common items in arrays. For example, intersection `([[ ‘a’, ‘b’ ], [ ‘b’, ‘c’ ], [ ‘b’, ‘d’]])` returns `[ ‘b’ ]`.

##### Declaration

```other
array intersection(array[array[any]] $sets)
```

##### Parameters

##### Return Value

A set that’s the intersect of the set representation of the arrays in `sets`.

## See Also

- [Converting arrays to sets](converting-arrays-to-sets.md)
  Return the content of a list, with duplicates removed and sorted, so that you can compare it to another set.
- [Computing numeric differences](computing-numeric-differences.md)
  Return the absolute difference between the maximum and minimum numerical values in an array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/intersecting-sets)*