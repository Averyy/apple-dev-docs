---
url: "https://docs.swift.org/latest/documentation/apiguidelines/parameter-names-for-documentation"
framework: "Swift-Org/APIGuidelines"
---

# Choose parameter names to serve documentation

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Choose parameter names to serve documentation.

#### Overview

Even though parameter names do not appear at a function or method’s point of use, they play an important explanatory role.

Parameter names appear in a function or method’s declaration:

```swift
func move(from **start**: Point, to **end**: Point)
```

Choose these names to make documentation easy to read.

✅ For example, these names make documentation read naturally:

```swift
/// Return an `Array` containing the elements of `self`
/// that satisfy `**predicate**`.
func filter(_ **predicate**: (Element) -> Bool) -> [Generator.Element]

/// Replace the given `**subRange**` of elements with `**newElements**`.
mutating func replaceRange(_ **subRange**: Range<Index>, with **newElements**: [E])
```

⛔ These, however, make the documentation awkward and ungrammatical:

```swift
/// Return an `Array` containing the elements of `self`
/// that satisfy `**includedInResult**`.
func filter(_ **includedInResult**: (Element) -> Bool) -> [Generator.Element]

/// Replace the **range of elements indicated by `r`** with
/// the contents of `**with**`.
mutating func replaceRange(_ **r**: Range<Index>, **with**: [E])
```

## See Also

### Conventions — Parameters
- [Take advantage of defaulted parameters](./defaulted-parameters.md)
  Take advantage of defaulted parameters when it simplifies common uses.
- [Locate parameters with defaults toward the end](./default-parameter-order.md)
  Prefer to locate parameters with defaults toward the end of the parameter list.
- [Prefer #fileID in production](./prefer-fileid.md)
  If your API will run in production, prefer `#fileID` over alternatives.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/parameter-names-for-documentation)*