---
url: "https://docs.swift.org/latest/documentation/apiguidelines/methods-over-free-functions"
framework: "Swift-Org/APIGuidelines"
---

# Prefer methods and properties to free functions

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

Prefer methods and properties to free functions.

## Overview

Free functions are used only in special cases:

1. When there’s no obvious `self`:

   ```
   min(x, y, z)
   ```
2. When the function is an unconstrained generic:

   ```
   print(x)
   ```
3. When function syntax is part of the established domain notation:

   ```
   sin(x)
   ```

## See Also

### Conventions — General
- [Document computed property complexity](./computed-property-complexity.md)
  Document the complexity of any computed property that is not O(1).
- [Follow case conventions](./case-conventions.md)
  Follow case conventions.
- [Methods can share a base name](./shared-base-names.md)
  Methods can share a base name when they share the same basic meaning or when they operate in distinct domains.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/methods-over-free-functions)*