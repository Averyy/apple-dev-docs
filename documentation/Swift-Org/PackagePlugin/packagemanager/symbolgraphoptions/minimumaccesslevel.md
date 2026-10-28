---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/minimumaccesslevel"
framework: "Swift-Org/PackagePlugin"
---

# minimumAccessLevel

**Framework**: Swift-Org/PackagePlugin  
**Kind**: property  
**Role**: Instance Property

The minimum access level of symbols to return.

## Declaration

```swift
var minimumAccessLevel: AccessLevel
```

## Discussion

The symbol graph includes symbols at this access level and higher.

## See Also

### Inspecting Symbol Graph Options
- [var emitExtensionBlocks: Bool](./emitextensionblocks.md)
  A Boolean value that indicates whether to emit symbols for extensions to external types.
- [var includeSPI: Bool](./includespi.md)
  A Boolean value that indicates whether to include symbols marked as SPI.
- [var includeSynthesized: Bool](./includesynthesized.md)
  A Boolean value that indicates whether to include synthesized members.
- [PackageManager.SymbolGraphOptions.AccessLevel](./accesslevel.md)
  The access level for a symbol.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/minimumaccesslevel)*