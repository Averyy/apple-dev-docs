---
url: "https://docs.swift.org/latest/documentation/apiguidelines/side-effect-naming"
framework: "Swift-Org/APIGuidelines"
---

# Name according to side-effects

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Name functions and methods according to their side-effects.

## Overview

- Those without side-effects should read as noun phrases, e.g. `x.distance(to: y)`, `i.successor()`.
- Those with side-effects should read as imperative verb phrases, e.g., `print(x)`, `x.sort()`, `x.append(y)`.
- Name mutating/nonmutating method pairs consistently. A mutating method will often have a nonmutating variant with similar semantics, but that returns a new value rather than updating an instance in-place.

  - When the operation is naturally described by a verb, use the verb’s imperative for the mutating method and apply the “ed” or “ing” suffix to name its nonmutating counterpart.

    | Mutating | Nonmutating |
    | --- | --- |
    | `x.sort()` | `z = x.sorted()` |
    | `x.append(y)` | `z = x.appending(y)` |

    - Prefer to name the nonmutating variant using the verb’s past [participle](https://en.wikipedia.org/wiki/Participle) (usually appending “ed”):

      ```swift
      /// Reverses `self` in-place.
      mutating func reverse()

      /// Returns a reversed copy of `self`.
      func revers**ed**() -> Self
      ...
      x.reverse()
      let y = x.reversed()
      ```
    - When adding “ed” is not grammatical because the verb has a direct object, name the nonmutating variant using the verb’s present [participle](https://en.wikipedia.org/wiki/Participle), by appending “ing.”

      ```swift
      /// Strips all the newlines from `self`
      mutating func stripNewlines()

      /// Returns a copy of `self` with all the newlines stripped.
      func strip**ping**Newlines() -> String
      ...
      s.stripNewlines()
      let oneLine = t.strippingNewlines()
      ```
  - When the operation is naturally described by a noun, use the noun for the nonmutating method and apply the “form” prefix to name its mutating counterpart.

    | Nonmutating | Mutating |
    | --- | --- |
    | `x = y.union(z)` | `y.formUnion(z)` |
    | `j = c.successor(i)` | `c.formSuccessor(&i)` |

## See Also

### Naming — Strive for Fluent Usage
- [Prefer grammatical English phrases](./grammatical-phrases.md)
  Prefer method and function names that make use sites form grammatical English phrases.
- [Begin factory method names with “make”](./factory-methods.md)
  Begin names of factory methods with “`make`.”
- [Initializer and factory method first arguments](./initializer-first-arguments.md)
  The first argument to initializer and factory method calls should not form a phrase starting with the base name.
- [Boolean methods read as assertions](./boolean-assertions.md)
  Uses of Boolean methods and properties should read as assertions about the receiver when the use is nonmutating.
- [Protocols describing “what” read as nouns](./protocol-nouns.md)
  Protocols that describe *what something is* should read as nouns.
- [Protocols describing capability use suffixes](./protocol-capability-suffixes.md)
  Protocols that describe a *capability* should be named using the suffixes `able`, `ible`, or `ing`.
- [Other names read as nouns](./noun-names.md)
  The names of other types, properties, variables, and constants should read as nouns.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/side-effect-naming)*