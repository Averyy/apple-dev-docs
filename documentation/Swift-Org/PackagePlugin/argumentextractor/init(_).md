---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/init(_:)"
framework: "Swift-Org/PackagePlugin"
---

# init(_:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: init  
**Role**: Initializer

Creates an argument extractor with a list of strings from which to extract flags and options.

## Declaration

```swift
init(_ arguments: [String])
```

#### Discussion

If the list contains `--`, any arguments that follow it are considered positional arguments.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/init(_:))*