---
url: "https://docs.swift.org/latest/documentation/embeddedswift/conditionalcompilation"
framework: "Swift-Org/EmbeddedSwift"
---

# Conditionalizing compilation for Embedded Swift

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article

Share code between Embedded Swift and full Swift using conditional compilation.

#### Overview

It’s often useful to have source code be compilable under both regular Swift and Embedded Swift. The following syntax is available for that (but note that as the rest of Embedded Swift, it’s experimental, subject to change and not considered source stable):

```swift
func sayHello() {
  #if hasFeature(Embedded)
  print("I'm Embedded Swift")
  #else
  print("I'm regular Swift")
  #endif
}
```

Additionally, you can also use an attribute (also experimental, and not source stable) to make entire functions, types and other declarations unavailable in Embedded Swift. This can be particularly useful to explicitly mark your own code (and also entire types and conformances) that relies on features unavailable in Embedded Swift, for example, the Any type or Codable – it is explicitly allowed to use those in unavailable contexts:

```swift
@_unavailableInEmbedded
func useAny(_: Any) { ... }

@_unavailableInEmbedded
extension MyStruct: Codable {
  ...
}
```

## See Also

### Language features
- [Reviewing the language subset](./languagesubset.md)
  Learn about the Embedded Swift language subset compared to full Swift.
- [Using strings](./strings.md)
  Enable full Unicode-compliant string support in Embedded Swift.
- [Using libraries and modules in Embedded Swift](./libraries.md)
  Learn about the library setup and linkage model of Embedded Swift.
- [Managing external dependencies](./externaldependencies.md)
  Learn what external system dependencies to expect from Embedded Swift compilations.
- [Working with existentials](./existentials.md)
  Learn about restrictions on existentials that apply in Embedded Swift.
- [Restricting non-final generic methods](./nonfinalgenericmethods.md)
  Learn why unbound generic methods aren’t allowed in Embedded Swift.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/conditionalcompilation)*