# subtract(_:)

**Framework**: PaperKit  
**Kind**: method

Removes the elements of the given set from this set.

## Declaration

```swift
mutating func subtract(_ other: Self)
```

#### Discussion

In the following example, the elements of the `employees` set that are also members of the `neighbors` set are removed. In particular, the names `"Bethany"` and `"Eric"` are removed from `employees`.

```None
var employees: Set = ["Alicia", "Bethany", "Chris", "Diana", "Eric"]
let neighbors: Set = ["Bethany", "Eric", "Forlani", "Greta"]
employees.subtract(neighbors)
print(employees)
// Prints "["Diana", "Chris", "Alicia"]"
```

## Parameters

- `other`: A set of the same type as the current set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/featureset/linemarkerpositions-swift.struct/subtract(_:))*