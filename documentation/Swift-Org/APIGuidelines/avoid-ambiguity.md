---
url: "https://docs.swift.org/latest/documentation/apiguidelines/avoid-ambiguity"
framework: "Swift-Org/APIGuidelines"
---

# Include words to avoid ambiguity

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Include all the words needed to avoid ambiguity for a person reading code where the name is used.

#### Overview

✅ For example, consider a method that removes the element at a given position within a collection.

```swift
extension List {
  public mutating func remove(at position: Index) -> Element
}
employees.remove(at: x)
```

⛔ If we were to omit the word `at` from the method signature, it could imply to the reader that the method searches for and removes an element equal to `x`, rather than using `x` to indicate the position of the element to remove.

```swift
employees.remove(x) // unclear: are we removing x?
```

## See Also

### Naming — Promote Clear Usage
- [Omit needless words](./omit-needless-words.md)
  Every word in a name should convey salient information at the use site.
- [Name according to roles](./name-according-to-roles.md)
  Name variables, parameters, and associated types according to their roles, rather than their type constraints.
- [Compensate for weak type information](./weak-type-information.md)
  Compensate for weak type information to clarify a parameter’s role.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/avoid-ambiguity)*