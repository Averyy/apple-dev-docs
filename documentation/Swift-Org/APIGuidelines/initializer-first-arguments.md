---
url: "https://docs.swift.org/latest/documentation/apiguidelines/initializer-first-arguments"
framework: "Swift-Org/APIGuidelines"
---

# Initializer and factory method first arguments

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

The first argument to initializer and factory method calls should not form a phrase starting with the base name.

## Overview

For example: `x.makeWidget(cogCount: 47)`.

For more on factory methods, see [Factory method pattern](https://en.wikipedia.org/wiki/Factory_method_pattern).

✅ For example, the first arguments to these calls do not read as part of the same phrase as the base name:

```swift
let foreground = **Color**(red: 32, green: 64, blue: 128)
let newPart = **factory.makeWidget**(gears: 42, spindles: 14)
let ref = **Link**(target: destination)
```

⛔ In the following, the API author has tried to create grammatical continuity with the first argument.

```swift
let foreground = **Color(havingRGBValuesRed: 32, green: 64, andBlue: 128)**
let newPart = **factory.makeWidget(havingGearCount: 42, andSpindleCount: 14)**
let ref = **Link(to: destination)**
```

In practice, this guideline along with those for argument labels (see [Omit labels for indistinguishable arguments](./indistinguishable-arguments.md)) means the first argument will have a label unless the call is performing a [value preserving type conversion](./value-preserving-conversions.md).

```swift
let rgbForeground = RGBColor(cmykForeground)
```

## See Also

### Naming — Strive for Fluent Usage
- [Prefer grammatical English phrases](./grammatical-phrases.md)
  Prefer method and function names that make use sites form grammatical English phrases.
- [Begin factory method names with “make”](./factory-methods.md)
  Begin names of factory methods with “`make`.”
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/initializer-first-arguments)*