---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/extractflag(named:)"
framework: "Swift-Org/PackagePlugin"
---

# extractFlag(named:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Extracts flags of the form `--<name>` from the remaining arguments, and returns the count.

## Declaration

```swift
mutating func extractFlag(named name: String) -> Int
```

## See Also

### Extracting Arguments
- [func extractOption(named: String) -> [String]](./extractoption%28named%29.md)
  Extracts options of the form `--<name> <value>` or `--<name>=<value>` from the remaining arguments and returns the extracted values.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/extractflag(named:))*