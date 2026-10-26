---
url: "https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/accesslevel"
framework: "Swift-Org/PackagePlugin"
---

# PackageManager.SymbolGraphOptions.AccessLevel

**Framework**: Swift-Org/PackagePlugin  
**Kind**: enum  
**Role**: Enumeration

The access level for a symbol.

## Declaration

```swift
enum AccessLevel
```

## Topics

### Access Levels
- [PackageManager.SymbolGraphOptions.AccessLevel.public](./accesslevel/public.md)
- [PackageManager.SymbolGraphOptions.AccessLevel.package](./accesslevel/package.md)
- [PackageManager.SymbolGraphOptions.AccessLevel.open](./accesslevel/open.md)
- [PackageManager.SymbolGraphOptions.AccessLevel.internal](./accesslevel/internal.md)
- [PackageManager.SymbolGraphOptions.AccessLevel.private](./accesslevel/private.md)
- [PackageManager.SymbolGraphOptions.AccessLevel.fileprivate](./accesslevel/fileprivate.md)
### Creating an Access Level
- [init?(rawValue: String)](./accesslevel/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./accesslevel/equatable-implementations.md)
- [RawRepresentable Implementations](./accesslevel/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.CaseIterable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable

## See Also

### Inspecting Symbol Graph Options
- [var emitExtensionBlocks: Bool](./emitextensionblocks.md)
  A Boolean value that indicates whether to emit symbols for extensions to external types.
- [var includeSPI: Bool](./includespi.md)
  A Boolean value that indicates whether to include symbols marked as SPI.
- [var includeSynthesized: Bool](./includesynthesized.md)
  A Boolean value that indicates whether to include synthesized members.
- [var minimumAccessLevel: AccessLevel](./minimumaccesslevel.md)
  The minimum access level of symbols to return.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/packageplugin/packagemanager/symbolgraphoptions/accesslevel)*