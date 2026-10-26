---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/extractoption(named:)"
framework: "Swift-Org/PackagePlugin"
---

# extractOption(named:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Extracts options of the form `--<name> <value>` or `--<name>=<value>` from the remaining arguments and returns the extracted values.

## Declaration

```swift
mutating func extractOption(named name: String) -> [String]
```

## See Also

### Extracting Arguments
- [func extractFlag(named: String) -> Int](./extractflag%28named%29.md)
  Extracts flags of the form `--<name>` from the remaining arguments, and returns the count.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/extractoption(named:))*