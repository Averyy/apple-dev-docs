# FilePath.Component

**Framework**: System  
**Kind**: struct  
**Role**: Structure

Represents an individual, non-root component of a file path.

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
struct Component
```

#### Overview

Components can be one of the special directory components (`.` or `..`) or a file or directory name. Components are never empty and never contain the directory separator.

Example:

```swift
var path: FilePath = "/tmp"
let file: FilePath.Component = "foo.txt"
file.kind == .regular           // true
file.extension                  // "txt"
path.append(file)               // path is "/tmp/foo.txt"
```

## Topics

### Initializers
- [init?(String)](./component/init%28_%29.md)
  Create a file path component from a string.
- [init?(platformString: [CInterop.PlatformChar])](./component/init%28platformstring%29-2tz4.md)
  Creates a file path component by copying bytes from a null-terminated platform string. It is a precondition that a null byte indicates the end of the string. The absence of a null byte will trigger a runtime error.
- [init?(platformString: inout CInterop.PlatformChar)](./component/init%28platformstring%29-3mzo3.md)
- [init?(platformString: String)](./component/init%28platformstring%29-8kixy.md)
- [init?(platformString: UnsafePointer<CInterop.PlatformChar>)](./component/init%28platformstring%29-9a3qq.md)
  Creates a file path component by copying bytes from a null-terminated platform string.
### Instance Properties
- [var `extension`: String?](./component/extension.md)
  The extension of this file or directory component.
- [var kind: FilePath.Component.Kind](./component/kind-swift.property.md)
  The kind of this component
- [var stem: String](./component/stem.md)
  The non-extension portion of this file or directory  component.
- [var string: String](./component/string.md)
  Creates a string by interpreting the component’s content as UTF-8 on Unix and UTF-16 on Windows.
### Instance Methods
- [func withPlatformString<Result>((UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result](./component/withplatformstring%28_%29.md)
  Calls the given closure with a pointer to the contents of the file path component, represented as a null-terminated platform string.
### Enumerations
- [FilePath.Component.Kind](./component/kind-swift.enum.md)
  Whether a component is a regular file or directory name, or a special directory `.` or `..`
### Default Implementations
- [CustomDebugStringConvertible Implementations](./component/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./component/customstringconvertible-implementations.md)
- [ExpressibleByStringLiteral Implementations](./component/expressiblebystringliteral-implementations.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath/component)*