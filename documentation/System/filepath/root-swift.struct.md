# FilePath.Root

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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

- Unix:

  - `/`
- Windows:

  - `C:\`
  - `C:`
  - `\`
  - `\\server\share\`
  - `\\?\UNC\server\share\`
  - `\\?\Volume{12345678-abcd-1111-2222-123445789abc}\`

## Topics

### Initializers
- [init?(String)](./root-swift.struct/init%28_%29.md)
  Create a file path root from a string.
- [init?(platformString: [CInterop.PlatformChar])](./root-swift.struct/init%28platformstring%29-3s0ol.md)
  Creates a file path root by copying bytes from a null-terminated platform string. It is a precondition that a null byte indicates the end of the string. The absence of a null byte will trigger a runtime error.
- [init?(platformString: String)](./root-swift.struct/init%28platformstring%29-4twb4.md)
- [init?(platformString: UnsafePointer<CInterop.PlatformChar>)](./root-swift.struct/init%28platformstring%29-5j1fu.md)
  Creates a file path root by copying bytes from a null-terminated platform string.
- [init?(platformString: inout CInterop.PlatformChar)](./root-swift.struct/init%28platformstring%29-8hwtb.md)
### Instance Properties
- [var string: String](./root-swift.struct/string.md)
  On Unix, this returns `"/"`.
### Instance Methods
- [func withPlatformString<Result>((UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result](./root-swift.struct/withplatformstring%28_%29.md)
  Calls the given closure with a pointer to the contents of the file path root, represented as a null-terminated platform string.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./root-swift.struct/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./root-swift.struct/customstringconvertible-implementations.md)
- [ExpressibleByStringLiteral Implementations](./root-swift.struct/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/root-swift.struct)*