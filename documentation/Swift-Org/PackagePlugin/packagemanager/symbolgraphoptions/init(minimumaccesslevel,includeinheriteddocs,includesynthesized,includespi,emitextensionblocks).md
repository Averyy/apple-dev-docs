---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/init(minimumaccesslevel:includeinheriteddocs:includesynthesized:includespi:emitextensionblocks:)"
framework: "Swift-Org/PackagePlugin"
---

# init(minimumAccessLevel:includeInheritedDocs:includeSynthesized:includeSPI:emitExtensionBlocks:)

**Framework**: Swift-Org/PackagePlugin  
**Kind**: init  
**Role**: Initializer

Creates a new set of options for returning the symbol graph for a target.

## Declaration

```swift
init(minimumAccessLevel: AccessLevel = .public, includeInheritedDocs: Bool = true, includeSynthesized: Bool = false, includeSPI: Bool = false, emitExtensionBlocks: Bool = false)
```

## Parameters

- `minimumAccessLevel`: The minimum access level of symbols to return.
- `includeInheritedDocs`: A Boolean value that indicates whether to include inheirted docs from protocol or class members.
- `includeSynthesized`: A Boolean value that indicates whether to include synthesized members.
- `includeSPI`: A Boolean value that indicates whether to include symbols marked as SPI.
- `emitExtensionBlocks`: A Boolean value that indicates whether to emit symbols for extensions to external types.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/init(minimumaccesslevel:includeinheriteddocs:includesynthesized:includespi:emitextensionblocks:))*