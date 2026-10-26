---
url: "https://docs.swift.org/latest/documentation/apiguidelines/name-according-to-roles"
framework: "Swift-Org/APIGuidelines"
---

# Name according to roles

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Name variables, parameters, and associated types according to their roles, rather than their type constraints.

#### Overview

⛔ Repurposing a type name fails to optimize clarity and expressivity:

```swift
var **string** = "Hello"
protocol ViewController {
  associatedtype **View**Type : View
}
class ProductionLine {
  func restock(from **widgetFactory**: WidgetFactory)
}
```

✅ Instead, strive to choose a name that expresses the entity’s *role*:

```swift
var **greeting** = "Hello"
protocol ViewController {
  associatedtype **ContentView** : View
}
class ProductionLine {
  func restock(from **supplier**: WidgetFactory)
}
```

If an associated type is so tightly bound to its protocol constraint that the protocol name *is* the role, avoid collision by appending `Protocol` to the protocol name:

```swift
protocol Sequence {
  associatedtype Iterator : Iterator**Protocol**
}
protocol Iterator**Protocol** { ... }
```

## See Also

### Naming — Promote Clear Usage
- [Include words to avoid ambiguity](./avoid-ambiguity.md)
  Include all the words needed to avoid ambiguity for a person reading code where the name is used.
- [Omit needless words](./omit-needless-words.md)
  Every word in a name should convey salient information at the use site.
- [Compensate for weak type information](./weak-type-information.md)
  Compensate for weak type information to clarify a parameter’s role.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/name-according-to-roles)*