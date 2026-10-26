---
url: "https://docs.swift.org/latest/documentation/apiguidelines/prefer-fileid"
framework: "Swift-Org/APIGuidelines"
---

# Prefer #fileID in production

**Framework**: Swift-Org/APIGuidelines  
**Role**: Article

If your API will run in production, prefer `#fileID` over alternatives.

#### Overview

`#fileID` saves space and protects developers’ privacy. Use `#filePath` in APIs that are never run by end users (such as test helpers and scripts) if the full path will simplify development workflows or be used for file I/O. Use `#file` to preserve source compatibility with Swift 5.2 or earlier.

## See Also

### Conventions — Parameters
- [Choose parameter names to serve documentation](./parameter-names-for-documentation.md)
  Choose parameter names to serve documentation.
- [Take advantage of defaulted parameters](./defaulted-parameters.md)
  Take advantage of defaulted parameters when it simplifies common uses.
- [Locate parameters with defaults toward the end](./default-parameter-order.md)
  Prefer to locate parameters with defaults toward the end of the parameter list.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/apiguidelines/prefer-fileid)*