---
url: "https://docs.swift.org/latest/documentation/apiguidelines/case-conventions"
framework: "Swift-Org/APIGuidelines"
---

# Follow case conventions

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Follow case conventions.

#### Overview

Names of types and protocols are `UpperCamelCase`. Everything else is `lowerCamelCase`.

[Acronyms and initialisms](https://en.wikipedia.org/wiki/Acronym) that commonly appear as all upper case in American English should be uniformly up- or down-cased according to case conventions:

```swift
var **utf8**Bytes: [**UTF8**.CodeUnit]
var isRepresentableAs**ASCII** = true
var user**SMTP**Server: Secure**SMTP**Server
```

Other acronyms should be treated as ordinary words:

```swift
var **radar**Detector: **Radar**Scanner
var enjoys**Scuba**Diving = true
```

## See Also

### Conventions — General
- [Document computed property complexity](./computed-property-complexity.md)
  Document the complexity of any computed property that is not O(1).
- [Prefer methods and properties to free functions](./methods-over-free-functions.md)
  Prefer methods and properties to free functions.
- [Methods can share a base name](./shared-base-names.md)
  Methods can share a base name when they share the same basic meaning or when they operate in distinct domains.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/case-conventions)*