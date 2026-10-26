---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphresult"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.SymbolGraphResult

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

The result of symbol graph generation.

## Declaration

```swift
struct SymbolGraphResult
```

## Topics

### Inspecting Symbol Graph Results
- [var directoryURL: URL](./symbolgraphresult/directoryurl.md)
  The file URL of the directory that contains the symbol graph files for the target.
- [var directoryPath: Path](./symbolgraphresult/directorypath.md)
  The directory that contains the symbol graph files for the target.

## See Also

### Retrieving Symbols for a Package
- [func getSymbolGraph(for: Target, options: SymbolGraphOptions) throws -> SymbolGraphResult](./getsymbolgraph%28for,options%29.md)
  Return a directory containing symbol graph files for the given target and options.
- [PackageManager.SymbolGraphOptions](./symbolgraphoptions.md)
  Represents options for symbol graph generation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphresult)*