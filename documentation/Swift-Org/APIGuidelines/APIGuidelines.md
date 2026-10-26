---
url: "https://docs.swift.org/latest/documentation/apiguidelines"
framework: "Swift-Org/APIGuidelines"
---

# API Guidelines

**Framework**: Swift-Org/APIGuidelines  
**Kind**: module

Design Swift APIs that prioritize clarity at the point of use through effective naming and consistent conventions.

#### Overview

Delivering a clear, consistent developer experience when writing Swift code is largely defined by the names and idioms that appear in APIs. These design guidelines explain how to make sure that your code feels like a part of the larger Swift ecosystem.

- **Clarity at the point of use** is your most important goal. Entities such as methods and properties are declared only once but *used* repeatedly.  Design APIs to make those uses clear and concise.  When evaluating a design, reading a declaration is seldom sufficient; always examine a use case to make sure it looks clear in context.
- **Clarity is more important than brevity.**  Although Swift code can be compact, it is a *non-goal* to enable the smallest possible code with the fewest characters. Brevity in Swift code, where it occurs, is a side-effect of the strong type system and features that naturally reduce boilerplate.
- **Write a documentation comment** for every declaration. Insights gained by writing documentation can have a profound impact on your design, so don’t put it off.

> ⚠️ **Warning**:  If you are having trouble describing your API’s functionality in simple terms, **you may have designed the wrong API.**

## Topics

### Fundamentals
- [Write a documentation comment for every declaration](./documentation-comments.md)
  Insights gained by writing documentation can have a profound impact on your design, so don’t put it off.
### Naming — Promote Clear Usage
- [Include words to avoid ambiguity](./avoid-ambiguity.md)
  Include all the words needed to avoid ambiguity for a person reading code where the name is used.
- [Omit needless words](./omit-needless-words.md)
  Every word in a name should convey salient information at the use site.
- [Name according to roles](./name-according-to-roles.md)
  Name variables, parameters, and associated types according to their roles, rather than their type constraints.
- [Compensate for weak type information](./weak-type-information.md)
  Compensate for weak type information to clarify a parameter’s role.
### Naming — Strive for Fluent Usage
- [Prefer grammatical English phrases](./grammatical-phrases.md)
  Prefer method and function names that make use sites form grammatical English phrases.
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
### Naming — Use Terminology Well
- [Avoid obscure terms](./avoid-obscure-terms.md)
  Avoid obscure terms if a more common word conveys meaning just as well.
- [Stick to the established meaning](./established-meaning.md)
  Stick to the established meaning if you do use a term of art.
- [Avoid abbreviations](./avoid-abbreviations.md)
  Avoid abbreviations.
- [Embrace precedent](./embrace-precedent.md)
  Embrace precedent.
### Conventions — General
- [Document computed property complexity](./computed-property-complexity.md)
  Document the complexity of any computed property that is not O(1).
- [Prefer methods and properties to free functions](./methods-over-free-functions.md)
  Prefer methods and properties to free functions.
- [Follow case conventions](./case-conventions.md)
  Follow case conventions.
- [Methods can share a base name](./shared-base-names.md)
  Methods can share a base name when they share the same basic meaning or when they operate in distinct domains.
### Conventions — Parameters
- [Choose parameter names to serve documentation](./parameter-names-for-documentation.md)
  Choose parameter names to serve documentation.
- [Take advantage of defaulted parameters](./defaulted-parameters.md)
  Take advantage of defaulted parameters when it simplifies common uses.
- [Locate parameters with defaults toward the end](./default-parameter-order.md)
  Prefer to locate parameters with defaults toward the end of the parameter list.
- [Prefer #fileID in production](./prefer-fileid.md)
  If your API will run in production, prefer `#fileID` over alternatives.
### Conventions — Argument Labels
- [Omit labels for indistinguishable arguments](./indistinguishable-arguments.md)
  Omit all labels when arguments can’t be usefully distinguished.
- [Omit first label for value-preserving type conversions](./value-preserving-conversions.md)
  In initializers that perform value preserving type conversions, omit the first argument label.
- [Label prepositional phrase arguments](./prepositional-phrase-labels.md)
  When the first argument forms part of a prepositional phrase, give it an argument label.
- [Omit label when first argument forms a grammatical phrase](./grammatical-phrase-arguments.md)
  Otherwise, if the first argument forms part of a grammatical phrase, omit its label, appending any preceding words to the base name.
- [Label all other arguments](./label-other-arguments.md)
  Label all other arguments.
### Special Instructions
- [Label tuple members and name closure parameters](./tuple-and-closure-labels.md)
  Label tuple members and name closure parameters where they appear in your API.
- [Take extra care with unconstrained polymorphism](./unconstrained-polymorphism.md)
  Take extra care with unconstrained polymorphism to avoid ambiguities in overload sets.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines)*