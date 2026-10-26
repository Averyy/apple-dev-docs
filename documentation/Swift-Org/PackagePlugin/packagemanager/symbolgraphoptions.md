---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.SymbolGraphOptions

**Framework**: Swift-Org/PackagePlugin  
**Kind**: struct  
**Role**: Structure

Represents options for symbol graph generation.

## Declaration

```swift
struct SymbolGraphOptions
```

## Topics

### Inspecting Symbol Graph Options
- [var emitExtensionBlocks: Bool](./symbolgraphoptions/emitextensionblocks.md)
  A Boolean value that indicates whether to emit symbols for extensions to external types.
- [var includeSPI: Bool](./symbolgraphoptions/includespi.md)
  A Boolean value that indicates whether to include symbols marked as SPI.
- [var includeSynthesized: Bool](./symbolgraphoptions/includesynthesized.md)
  A Boolean value that indicates whether to include synthesized members.
- [var minimumAccessLevel: AccessLevel](./symbolgraphoptions/minimumaccesslevel.md)
  The minimum access level of symbols to return.
- [PackageManager.SymbolGraphOptions.AccessLevel](./symbolgraphoptions/accesslevel.md)
  The access level for a symbol.
### Initializers
- [init(minimumAccessLevel: AccessLevel, includeInheritedDocs: Bool, includeSynthesized: Bool, includeSPI: Bool, emitExtensionBlocks: Bool)](./symbolgraphoptions/init%28minimumaccesslevel,includeinheriteddocs,includesynthesized,includespi,emitextensionblocks%29.md)
  Creates a new set of options for returning the symbol graph for a target.
### Instance Properties
- [var includeInheritedDocs: Bool](./symbolgraphoptions/includeinheriteddocs.md)
  A Boolean value that indicates whether to include inherited docs from class or protocol members.

## See Also

### Retrieving Symbols for a Package
- [func getSymbolGraph(for: Target, options: SymbolGraphOptions) throws -> SymbolGraphResult](./getsymbolgraph%28for,options%29.md)
  Return a directory containing symbol graph files for the given target and options.
- [PackageManager.SymbolGraphResult](./symbolgraphresult.md)
  The result of symbol graph generation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions)*