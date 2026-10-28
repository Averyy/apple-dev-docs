---
url: "https://docs.swift.org/latest/documentation/apiguidelines/grammatical-phrases"
framework: "Swift-Org/APIGuidelines"
---

# Prefer grammatical English phrases

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Prefer method and function names that make use sites form grammatical English phrases.

## Overview

✅ Each of these reads as a grammatical English phrase at the call site:

```swift
x.insert(y, at: z)          // "x, insert y at z"
x.subviews(havingColor: y)  // "x's subviews having color y"
x.capitalizingNouns()       // "x, capitalizing nouns"
```

⛔ Each of these drops the words that make the phrase grammatical, so the call no longer reads as English:

```swift
x.insert(y, position: z)
x.subviews(color: y)
x.nounCapitalize()
```

It is acceptable for fluency to degrade after the first argument or two when those arguments are not central to the call’s meaning:

```swift
AudioUnit.instantiate(
  with: description,
  **options: [.inProcess], completionHandler: stopProgressBar**)
```

## See Also

### Naming — Strive for Fluent Usage
- [Begin factory method names with “make”](./factory-methods.md)
  Begin names of factory methods with “`make`.”
- [Initializer and factory method first arguments](./initializer-first-arguments.md)
  The first argument to initializer and factory method calls should not form a phrase starting with the base name.
- [Name according to side-effects](./side-effect-naming.md)
  Name functions and methods according to their side-effects.
- [Boolean methods read as assertions](./boolean-assertions.md)
  Uses of Boolean methods and properties should read as assertions about the receiver when the use is nonmutating.
- [Protocols describing “what” read as nouns](./protocol-nouns.md)
  Protocols that describe *what something is* should read as nouns.
- [Protocols describing capability use suffixes](./protocol-capability-suffixes.md)
  Protocols that describe a *capability* should be named using the suffixes `able`, `ible`, or `ing`.
- [Other names read as nouns](./noun-names.md)
  The names of other types, properties, variables, and constants should read as nouns.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/grammatical-phrases)*