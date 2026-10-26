---
url: "https://docs.swift.org/latest/documentation/apiguidelines/weak-type-information"
framework: "Swift-Org/APIGuidelines"
---

# Compensate for weak type information

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Compensate for weak type information to clarify a parameter’s role.

#### Overview

Especially when a parameter type is `NSObject`, `Any`, `AnyObject`, or a fundamental type such as `Int` or `String`, type information and context at the point of use may not fully convey intent. In this example, the declaration may be clear, but the use site is vague.

⛔ Neither parameter name compensates for the weak `NSObject` and `String` types, so the call site reads as vague:

```swift
func add(_ observer: NSObject, for keyPath: String)

grid.add(self, for: graphics) // vague
```

✅ To restore clarity, precede each weakly typed parameter with a noun describing its role:

```swift
func add**Observer**(_ observer: NSObject, for**KeyPath** path: String)
grid.addObserver(self, forKeyPath: graphics) // clear
```

## See Also

### Naming — Promote Clear Usage
- [Include words to avoid ambiguity](./avoid-ambiguity.md)
  Include all the words needed to avoid ambiguity for a person reading code where the name is used.
- [Omit needless words](./omit-needless-words.md)
  Every word in a name should convey salient information at the use site.
- [Name according to roles](./name-according-to-roles.md)
  Name variables, parameters, and associated types according to their roles, rather than their type constraints.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/weak-type-information)*