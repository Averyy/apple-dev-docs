# Computing numeric differences

**Framework**: App Store Connect API

Return the absolute difference between the maximum and minimum numerical values in an array.

#### Overview

Use the `diff()` function in the expression of a matchmaking rule to compute the greatest difference between two or more values. For example, `diff([ `4`, `3`, `2`, `1` ])` returns `3`, and  `diff([ `50`, `19`, `21`, `61` ]` returns `42`.

##### Declaration

```other
number diff(array[number] $values)
```

##### Parameters

##### Return Value

The absolute difference between the maximum and minimum items in the `values` array.

## See Also

- [Converting arrays to sets](converting-arrays-to-sets.md)
  Return the content of a list, with duplicates removed and sorted, so that you can compare it to another set.
- [Intersecting sets](intersecting-sets.md)
  Return the intersection of two or more arrays treated as sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/computing-numeric-differences)*