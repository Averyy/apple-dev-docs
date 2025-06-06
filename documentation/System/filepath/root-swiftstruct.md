# FilePath.Root

**Framework**: System  
**Kind**: struct

Represents a root of a file path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct Root
```

#### Overview

On Unix, a root is simply the directory separator `/`.

On Windows, a root contains the entire path prefix up to and including the final separator.

Examples:

- Unix: - `/`
- Windows: - `C:\`
- `C:`
- `\`
- `\\server\share\`
- `\\?\UNC\server\share\`
- `\\?\Volume{12345678-abcd-1111-2222-123445789abc}\`

## Topics

### Initializers
- [init?(String)](filepath/root-swift.struct/init(_:).md)
  Create a file path root from a string.
- [init?(platformString: [CInterop.PlatformChar])](filepath/root-swift.struct/init(platformstring:)-3s0ol.md)
  Creates a file path root by copying bytes from a null-terminated platform string. It is a precondition that a null byte indicates the end of the string. The absence of a null byte will trigger a runtime error.
- [init?(platformString: String)](filepath/root-swift.struct/init(platformstring:)-4twb4.md)
- [init?(platformString: UnsafePointer<CInterop.PlatformChar>)](filepath/root-swift.struct/init(platformstring:)-5j1fu.md)
  Creates a file path root by copying bytes from a null-terminated platform string.
- [init?(platformString: inout CInterop.PlatformChar)](filepath/root-swift.struct/init(platformstring:)-8hwtb.md)
### Instance Properties
- [var string: String](filepath/root-swift.struct/string.md)
  On Unix, this returns `"/"`.
### Instance Methods
- [func withPlatformString<Result>((UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result](filepath/root-swift.struct/withplatformstring(_:).md)
  Calls the given closure with a pointer to the contents of the file path root, represented as a null-terminated platform string.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filepath/root-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filepath/root-swift.struct/customstringconvertible-implementations.md)
- [Decodable Implementations](filepath/root-swift.struct/decodable-implementations.md)
- [Encodable Implementations](filepath/root-swift.struct/encodable-implementations.md)
- [Equatable Implementations](filepath/root-swift.struct/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](filepath/root-swift.struct/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](filepath/root-swift.struct/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](filepath/root-swift.struct/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](filepath/root-swift.struct/hashable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.struct)*