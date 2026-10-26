---
url: "https://docs.swift.org/latest/documentation/apiguidelines/omit-needless-words"
framework: "Swift-Org/APIGuidelines"
---

# Omit needless words

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Every word in a name should convey salient information at the use site.

#### Overview

More words may be needed to clarify intent or disambiguate meaning, but those that are redundant with information the reader already possesses should be omitted. In particular, omit words that *merely repeat* type information.

⛔ In this case, the word `Element` adds nothing salient at the call site:

```swift
public mutating func removeElement(_ member: Element) -> Element?

allViews.removeElement(cancelButton)
```

✅ This API would be better:

```swift
public mutating func remove(_ member: Element) -> Element?

allViews.remove(cancelButton) // clearer
```

Occasionally, repeating type information is necessary to avoid ambiguity, but in general it is better to use a word that describes a parameter’s *role* rather than its type. See [Name according to roles](./name-according-to-roles.md) for details.

## See Also

### Naming — Promote Clear Usage
- [Include words to avoid ambiguity](./avoid-ambiguity.md)
  Include all the words needed to avoid ambiguity for a person reading code where the name is used.
- [Name according to roles](./name-according-to-roles.md)
  Name variables, parameters, and associated types according to their roles, rather than their type constraints.
- [Compensate for weak type information](./weak-type-information.md)
  Compensate for weak type information to clarify a parameter’s role.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/omit-needless-words)*