---
url: "https://docs.swift.org/latest/documentation/apiguidelines/indistinguishable-arguments"
framework: "Swift-Org/APIGuidelines"
---

# Omit labels for indistinguishable arguments

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Omit all labels when arguments can’t be usefully distinguished.

## Overview

For example: `min(number1, number2)`, `zip(sequence1, sequence2)`.

Argument labels appear at a function or method’s point of use:

```swift
func move(**from** start: Point, **to** end: Point)
x.move(**from:** x, **to:** y)
```

## See Also

### Conventions — Argument Labels
- [Omit first label for value-preserving type conversions](./value-preserving-conversions.md)
  In initializers that perform value preserving type conversions, omit the first argument label.
- [Label prepositional phrase arguments](./prepositional-phrase-labels.md)
  When the first argument forms part of a prepositional phrase, give it an argument label.
- [Omit label when first argument forms a grammatical phrase](./grammatical-phrase-arguments.md)
  Otherwise, if the first argument forms part of a grammatical phrase, omit its label, appending any preceding words to the base name.
- [Label all other arguments](./label-other-arguments.md)
  Label all other arguments.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/indistinguishable-arguments)*