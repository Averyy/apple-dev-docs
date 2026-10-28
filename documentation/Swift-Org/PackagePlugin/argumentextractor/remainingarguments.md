---
url: "https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/remainingarguments"
framework: "Swift-Org/PackagePlugin"
---

# remainingArguments

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

Returns all remaining arguments.

## Declaration

```swift
var remainingArguments: [String] { get }
```

## Discussion

The returned values include any positional arguments after the first `--`, if there is one.

## See Also

### Inspecting Arguments
- [var unextractedOptionsOrFlags: [String]](./unextractedoptionsorflags.md)
  Returns any unextracted flags or options.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/argumentextractor/remainingarguments)*