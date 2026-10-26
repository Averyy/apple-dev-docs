---
url: "https://docs.swift.org/latest/documentation/apiguidelines/computed-property-complexity"
framework: "Swift-Org/APIGuidelines"
---

# Document computed property complexity

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Document the complexity of any computed property that is not O(1).

#### Overview

People often assume that property access involves no significant computation, because they have stored properties as a mental model. Be sure to alert them when that assumption may be violated.

## See Also

### Conventions — General
- [Prefer methods and properties to free functions](./methods-over-free-functions.md)
  Prefer methods and properties to free functions.
- [Follow case conventions](./case-conventions.md)
  Follow case conventions.
- [Methods can share a base name](./shared-base-names.md)
  Methods can share a base name when they share the same basic meaning or when they operate in distinct domains.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/computed-property-complexity)*