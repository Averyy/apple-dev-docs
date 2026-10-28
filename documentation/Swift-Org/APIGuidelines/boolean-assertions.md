---
url: "https://docs.swift.org/latest/documentation/apiguidelines/boolean-assertions"
framework: "Swift-Org/APIGuidelines"
---

# Boolean methods read as assertions

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Uses of Boolean methods and properties should read as assertions about the receiver when the use is nonmutating.

## Overview

For example: `x.isEmpty`, `line1.intersects(line2)`.

## See Also

### Naming — Strive for Fluent Usage
- [Prefer grammatical English phrases](./grammatical-phrases.md)
  Prefer method and function names that make use sites form grammatical English phrases.
- [Begin factory method names with “make”](./factory-methods.md)
  Begin names of factory methods with “`make`.”
- [Initializer and factory method first arguments](./initializer-first-arguments.md)
  The first argument to initializer and factory method calls should not form a phrase starting with the base name.
- [Name according to side-effects](./side-effect-naming.md)
  Name functions and methods according to their side-effects.
- [Protocols describing “what” read as nouns](./protocol-nouns.md)
  Protocols that describe *what something is* should read as nouns.
- [Protocols describing capability use suffixes](./protocol-capability-suffixes.md)
  Protocols that describe a *capability* should be named using the suffixes `able`, `ible`, or `ing`.
- [Other names read as nouns](./noun-names.md)
  The names of other types, properties, variables, and constants should read as nouns.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/boolean-assertions)*