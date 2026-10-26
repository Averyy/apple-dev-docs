---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/getsymbolgraph(for:options:)"
framework: "Swift-Org/PackagePlugin"
---

# getSymbolGraph(for:options:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: method  
**Role**: Instance Method

Return a directory containing symbol graph files for the given target and options.

## Declaration

```swift
func getSymbolGraph(for target: Target, options: SymbolGraphOptions) throws -> SymbolGraphResult
```

#### Return Value

The symbol graphs for the target you specify.

#### Discussion

If the symbol graphs need to be created or updated first, they will be. Swift package manager or an IDE may generate these symbol graph files in any way it sees fit.

## Parameters

- `target`: The target to build or from which to extract symbol graphs.
- `options`: The options to use while building or extracting symbol graphs.

## See Also

### Retrieving Symbols for a Package
- [PackageManager.SymbolGraphOptions](./symbolgraphoptions.md)
  Represents options for symbol graph generation.
- [PackageManager.SymbolGraphResult](./symbolgraphresult.md)
  The result of symbol graph generation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/getsymbolgraph(for:options:))*