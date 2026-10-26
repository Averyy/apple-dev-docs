---
url: "https://docs.swift.org/latest/documentation/apiguidelines/value-preserving-conversions"
framework: "Swift-Org/APIGuidelines"
---

# Omit first label for value-preserving type conversions

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

In initializers that perform value preserving type conversions, omit the first argument label.

#### Overview

For example: `Int64(someUInt32)`.

The first argument should always be the source of the conversion.

```
extension String {
  // Convert `x` into its textual representation in the given radix
  init(**_** x: BigInt, radix: Int = 10)   // ← Note the initial underscore
}

text = "The value is: "
text += **String(veryLargeNumber)**
text += " and in hexadecimal, it's"
text += **String(veryLargeNumber, radix: 16)**
```

In “narrowing” type conversions, though, a label that describes the narrowing is recommended.

```swift
extension UInt32 {
  /// Creates an instance having the specified `value`.
  init(**_** value: Int16)            // ← Widening, so no label
  /// Creates an instance having the lowest 32 bits of `source`.
  init(**truncating** source: UInt64)
  /// Creates an instance having the nearest representable
  /// approximation of `valueToApproximate`.
  init(**saturating** valueToApproximate: UInt64)
}
```

> **Note**: A value preserving type conversion is a [monomorphism](https://en.wikipedia.org/wiki/Monomorphism), i.e. every difference in the value of the source results in a difference in the value of the result. For example, conversion from `Int8` to `Int64` is value preserving because every distinct `Int8` value is converted to a distinct `Int64` value.  Conversion in the other direction, however, cannot be value preserving: `Int64` has more possible values than can be represented in an `Int8`.
>
> Note: the ability to retrieve the original value has no bearing on whether a conversion is value preserving.

## See Also

### Conventions — Argument Labels
- [Omit labels for indistinguishable arguments](./indistinguishable-arguments.md)
  Omit all labels when arguments can’t be usefully distinguished.
- [Label prepositional phrase arguments](./prepositional-phrase-labels.md)
  When the first argument forms part of a prepositional phrase, give it an argument label.
- [Omit label when first argument forms a grammatical phrase](./grammatical-phrase-arguments.md)
  Otherwise, if the first argument forms part of a grammatical phrase, omit its label, appending any preceding words to the base name.
- [Label all other arguments](./label-other-arguments.md)
  Label all other arguments.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/value-preserving-conversions)*