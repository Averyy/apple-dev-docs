# SymbolicatedFrame

**Framework**: CrashReportExtension  
**Kind**: struct

A type that represents a single symbolicated stack frame.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SymbolicatedFrame
```

## Topics

### Creating a symbolicated frame
- [init(symbol: String, symbolOffset: UInt64, sourceFile: String?, sourceLine: Int?, isInline: Bool)](symbolicatedframe/init(symbol:symboloffset:sourcefile:sourceline:isinline:).md)
### Accessing symbolicated frame properties
- [let sourceFile: String?](symbolicatedframe/sourcefile.md)
  The name of the source file, if available.
- [let sourceLine: Int?](symbolicatedframe/sourceline.md)
  The line number within the source file, if available.
- [let symbol: String](symbolicatedframe/symbol.md)
  The symbol associated with the stack frame.
- [let symbolOffset: UInt64](symbolicatedframe/symboloffset.md)
  The symbol offset within the frame.
- [let isInline: Bool](symbolicatedframe/isinline.md)
  A flag that indicates if the stack frame is inline.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func symbolicateAddress(UInt64) -> [SymbolicatedFrame]](crashedprocess/symbolicateaddress(_:).md)
  Symbolicates an address, returning symbol info with inline frame expansion.
- [func symbolicateAddresses([UInt64]) -> [[SymbolicatedFrame]]](crashedprocess/symbolicateaddresses(_:).md)
  Symbolicates an array of addresses, returning symbol information with inline frame expansion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/crashreportextension/symbolicatedframe)*