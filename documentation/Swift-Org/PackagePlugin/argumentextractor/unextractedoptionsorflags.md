---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/unextractedoptionsorflags"
framework: "Swift-Org/PackagePlugin"
---

# unextractedOptionsOrFlags

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Returns any unextracted flags or options.

## Declaration

```swift
var unextractedOptionsOrFlags: [String] { get }
```

#### Discussion

This is based strictly on whether remaining arguments have a `--` prefix.

## See Also

### Inspecting Arguments
- [var remainingArguments: [String]](./remainingarguments.md)
  Returns all remaining arguments.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/unextractedoptionsorflags)*