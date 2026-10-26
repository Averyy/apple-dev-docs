---
url: "https://docs.swift.org/latest/documentation/apiguidelines/prepositional-phrase-labels"
framework: "Swift-Org/APIGuidelines"
---

# Label prepositional phrase arguments

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

When the first argument forms part of a prepositional phrase, give it an argument label.

#### Overview

The argument label should normally begin at the preposition. For example: `x.removeBoxes(havingLength: 12)`.

For more on prepositional phrases, see [prepositional phrase](https://en.wikipedia.org/wiki/Adpositional_phrase#Prepositional_phrases). For more on prepositions, see [preposition](https://en.wikipedia.org/wiki/Preposition).

An exception arises when the first two arguments represent parts of a single abstraction.

⛔ Splitting the label across both arguments breaks the single abstraction into two disconnected phrases:

```swift
a.move(**toX:** b, **y:** c)
a.fade(**fromRed:** b, **green:** c, **blue:** d)
```

✅ In such cases, begin the argument label *after* the preposition, to keep the abstraction clear.

```swift
a.moveTo(**x:** b, **y:** c)
a.fadeFrom(**red:** b, **green:** c, **blue:** d)
```

## See Also

### Conventions — Argument Labels
- [Omit labels for indistinguishable arguments](./indistinguishable-arguments.md)
  Omit all labels when arguments can’t be usefully distinguished.
- [Omit first label for value-preserving type conversions](./value-preserving-conversions.md)
  In initializers that perform value preserving type conversions, omit the first argument label.
- [Omit label when first argument forms a grammatical phrase](./grammatical-phrase-arguments.md)
  Otherwise, if the first argument forms part of a grammatical phrase, omit its label, appending any preceding words to the base name.
- [Label all other arguments](./label-other-arguments.md)
  Label all other arguments.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/prepositional-phrase-labels)*