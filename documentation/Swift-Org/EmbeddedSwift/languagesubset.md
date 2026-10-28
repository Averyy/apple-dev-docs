---
url: "https://docs.swift.org/latest/documentation/embeddedswift/languagesubset"
framework: "Swift-Org/EmbeddedSwift"
---

# Reviewing the language subset

**Framework**: Swift-Org/EmbeddedSwift  
**Role**: Article

Learn about the Embedded Swift language subset compared to full Swift.

## Overview

Embedded Swift is a subset of the Swift language, and some features are not available in Embedded Swift. This is necessary in order to achieve small binaries with effective dead-code elimination and minimized system dependencies.

That said, *the vast majority* of the Swift language works exactly the same in Embedded Swift. This includes generics, protocols, enums with associated values, tuples, optionals, classes (instances are allocated on the heap and refcounted just like in regular Swift), inheritance, runtime polymorphism, arrays (heap-allocated copy-on-write just like in regular Swift) and much more.

Note that there are no behavior changes in Embedded Swift compared to full Swift, and Embedded Swift is strictly a *subset* and not a *dialect*. Any code compatible with Embedded Swift will also compile and have the same semantics in full Swift.

## Code-level features that are not available

- **Not available**: Runtime reflection (`Mirror` APIs).
- **Not available**: Calling generic functions on values of protocol type (“existentials”). See [Working with existentials](./existentials.md) for details.
- **Not available**: Standard library types that rely on the above, for example `Codable`, are not allowed.
- **Not available**: Printing and stringification of arbitrary types (which is achieved through reflection in desktop Swift).
- **Not available**: Using non-final generic class methods. See [Restricting non-final generic methods](./nonfinalgenericmethods.md) for details on this.
- **Not available**: Weak and unowned references are not allowed (unsafe unowned references *are* available).

## Compilation facilities that are not available

- **Not available**: Library Evolution (stable ABI), and facilities that requires Library Evolution (for example, internal module imports)
- **Not available**: Objective-C interoperability
- **Not available**: Builds without WMO (whole module optimization)

## Further resources

The above lists are describing features that are removed from Embedded Swift *by design*. Since Embedded Swift is currently an experimental preview, there might also be  features that are not yet implemented. See the in-development status at [Tracking implementation status](./status.md).

## See Also

### Language features
- [Using strings](./strings.md)
  Enable full Unicode-compliant string support in Embedded Swift.
- [Conditionalizing compilation for Embedded Swift](./conditionalcompilation.md)
  Share code between Embedded Swift and full Swift using conditional compilation.
- [Using libraries and modules in Embedded Swift](./libraries.md)
  Learn about the library setup and linkage model of Embedded Swift.
- [Managing external dependencies](./externaldependencies.md)
  Learn what external system dependencies to expect from Embedded Swift compilations.
- [Working with existentials](./existentials.md)
  Learn about restrictions on existentials that apply in Embedded Swift.
- [Restricting non-final generic methods](./nonfinalgenericmethods.md)
  Learn why unbound generic methods aren’t allowed in Embedded Swift.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/embeddedswift/languagesubset)*