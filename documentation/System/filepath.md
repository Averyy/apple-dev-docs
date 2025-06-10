# FilePath

**Framework**: System  
**Kind**: struct

Represents a location in the file system.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
struct FilePath
```

#### Overview

This structure recognizes directory separators  (e.g. `/`), roots, and requires that the content terminates in a NUL (`0x0`). Beyond that, it does not give any meaning to the bytes that it contains. The file system defines how the content is interpreted; for example, by its choice of string encoding.

On construction, `FilePath` will normalize separators by removing redundant intermediary separators and stripping any trailing separators. On Windows, `FilePath` will also normalize forward slashes `/` into backslashes `\`, as preferred by the platform.

The code below creates a file path from a string literal, and then uses it to open and append to a log file:

```swift
let message: String = "This is a log message."
let path: FilePath = "/tmp/log"
let fd = try FileDescriptor.open(path, .writeOnly, options: .append)
try fd.closeAfter { try fd.writeAll(message.utf8) }
```

File paths conform to the [`Equatable`](https://developer.apple.com/documentation/Swift/Equatable) and [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocols by performing the protocols’ operations on their raw byte contents. This conformance allows file paths to be used, for example, as keys in a dictionary. However, the rules for path equivalence are file-system–specific and have additional considerations like case insensitivity, Unicode normalization, and symbolic links.

## Topics

### Creating a File Path
- [init()](filepath/init.md)
  Creates an empty, null-terminated path.
- [init(stringLiteral: String)](filepath/init(stringliteral:).md)
  Creates a file path from a string literal.
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](filepath/init(extendedgraphemeclusterliteral:).md)
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](filepath/init(unicodescalarliteral:).md)
### Working with File Paths
- [var length: Int](filepath/length.md)
  The length of the file path, excluding the null terminator.
- [var description: String](filepath/description.md)
  A textual representation of the file path.
- [var debugDescription: String](filepath/debugdescription.md)
  A textual representation of the file path, suitable for debugging.
### Interacting with C APIs
- [func withCString<Result>((UnsafePointer<CChar>) throws -> Result) rethrows -> Result](filepath/withcstring(_:).md)
  For backwards compatibility only. This function is equivalent to the preferred `withPlatformString`.
### Comparing File Paths
- [static func == (FilePath, FilePath) -> Bool](filepath/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](filepath/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filepath/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](filepath/hashvalue.md)
  The hash value.
### Encoding File Paths
- [init(from: any Decoder) throws](filepath/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](filepath/encode(to:).md)
  Encodes this value into the given encoder.
### Structures
- [FilePath.Component](filepath/component.md)
  Represents an individual, non-root component of a file path.
- [FilePath.ComponentView](filepath/componentview.md)
  A bidirectional, range replaceable collection of the non-root components that make up a file path.
- [FilePath.Root](filepath/root-swift.struct.md)
  Represents a root of a file path.
### Initializers
- [init?(URL)](filepath/init(_:)-2gkpw.md)
  Creates a file path from a URL
- [init(String)](filepath/init(_:)-61dsw.md)
  Creates a file path from a string.
- [init(cString: [CChar])](filepath/init(cstring:)-2hetg.md)
- [init(cString: String)](filepath/init(cstring:)-3xw0n.md)
- [init(cString: UnsafePointer<CChar>)](filepath/init(cstring:)-5igtz.md)
  For backwards compatibility only. This initializer is equivalent to the preferred `FilePath(platformString:)`.
- [init(cString: inout CChar)](filepath/init(cstring:)-8d3vx.md)
- [init(platformString: inout CInterop.PlatformChar)](filepath/init(platformstring:)-4b3o6.md)
- [init(platformString: UnsafePointer<CInterop.PlatformChar>)](filepath/init(platformstring:)-5o7oh.md)
  Creates a file path by copying bytes from a null-terminated platform string.
- [init(platformString: String)](filepath/init(platformstring:)-6i5cc.md)
- [init(platformString: [CInterop.PlatformChar])](filepath/init(platformstring:)-8amn5.md)
  Creates a file path by copying bytes from a null-terminated platform string.
- [init<C>(root: FilePath.Root?, C)](filepath/init(root:_:)-19uu0.md)
  Create a file path from a root and a collection of components.
- [init(root: FilePath.Root?, FilePath.ComponentView.SubSequence)](filepath/init(root:_:)-19xzy.md)
  Create a file path from an optional root and a slice of another path’s components.
- [init(root: FilePath.Root?, components: FilePath.Component...)](filepath/init(root:components:).md)
  Create a file path from a root and any number of components.
### Instance Properties
- [var components: FilePath.ComponentView](filepath/components.md)
  View the non-root components that make up this path.
- [var `extension`: String?](filepath/extension.md)
  The extension of the file or directory last component.
- [var isAbsolute: Bool](filepath/isabsolute.md)
  Returns true if this path uniquely identifies the location of a file without reference to an additional starting location.
- [var isEmpty: Bool](filepath/isempty.md)
  Whether this path is empty
- [var isLexicallyNormal: Bool](filepath/islexicallynormal.md)
  Whether the path is in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks).
- [var isRelative: Bool](filepath/isrelative.md)
  Returns true if this path is not absolute (see `isAbsolute`).
- [var lastComponent: FilePath.Component?](filepath/lastcomponent.md)
  Returns the final component of the path. Returns `nil` if the path is empty or only contains a root.
- [var root: FilePath.Root?](filepath/root-swift.property.md)
  Returns the root of a path if there is one, otherwise `nil`.
- [var stem: String?](filepath/stem.md)
  The non-extension portion of the file or directory last component.
- [var string: String](filepath/string.md)
  Creates a string by interpreting the path’s content as UTF-8 on Unix and UTF-16 on Windows.
### Instance Methods
- [func append<C>(C)](filepath/append(_:)-66nkr.md)
  Append `components` on to the end of this path.
- [func append(String)](filepath/append(_:)-7ttzp.md)
  Append the contents of `other`, ignoring any spurious leading separators.
- [func append(FilePath.Component)](filepath/append(_:)-8f41n.md)
  Append a `component` on to the end of this path.
- [func appending(String) -> FilePath](filepath/appending(_:)-1dtn3.md)
  Non-mutating version of `append(_:String)`.
- [func appending(FilePath.Component) -> FilePath](filepath/appending(_:)-24s87.md)
  Non-mutating version of `append(_:Component)`.
- [func appending<C>(C) -> FilePath](filepath/appending(_:)-60fwk.md)
  Non-mutating version of `append(_:C)`.
- [func ends(with: FilePath) -> Bool](filepath/ends(with:).md)
  Returns whether `other` is a suffix of `self`, only considering whole path components.
- [func lexicallyNormalize()](filepath/lexicallynormalize.md)
  Collapse `.` and `..` components lexically (i.e. without following symlinks).
- [func lexicallyNormalized() -> FilePath](filepath/lexicallynormalized.md)
  Returns a copy of `self` in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks). See `lexicallyNormalize`
- [func lexicallyResolving(FilePath) -> FilePath?](filepath/lexicallyresolving(_:).md)
  Create a new `FilePath` by resolving `subpath` relative to `self`, ensuring that the result is lexically contained within `self`.
- [func push(FilePath)](filepath/push(_:).md)
  If `other` does not have a root, append each component of `other`. If `other` has a root, replaces `self` with other.
- [func pushing(FilePath) -> FilePath](filepath/pushing(_:).md)
  Non-mutating version of `push()`.
- [func removeAll(keepingCapacity: Bool)](filepath/removeall(keepingcapacity:).md)
  Remove the contents of the path, keeping the null terminator.
- [func removeLastComponent() -> Bool](filepath/removelastcomponent.md)
  In-place mutating variant of `removingLastComponent`.
- [func removePrefix(FilePath) -> Bool](filepath/removeprefix(_:).md)
  If `prefix` is a prefix of `self`, removes it and returns `true`. Otherwise returns `false`.
- [func removingLastComponent() -> FilePath](filepath/removinglastcomponent.md)
  Creates a new path with everything up to but not including `lastComponent`.
- [func removingRoot() -> FilePath](filepath/removingroot.md)
  Creates a new path containing just the components, i.e. everything after `root`.
- [func reserveCapacity(Int)](filepath/reservecapacity(_:).md)
  Reserve enough storage space to store `minimumCapacity` platform characters.
- [func starts(with: FilePath) -> Bool](filepath/starts(with:).md)
  Returns whether `other` is a prefix of `self`, only considering whole path components.
- [func withPlatformString<Result>((UnsafePointer<CInterop.PlatformChar>) throws -> Result) rethrows -> Result](filepath/withplatformstring(_:).md)
  Calls the given closure with a pointer to the contents of the file path, represented as a null-terminated platform string.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filepath/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filepath/customstringconvertible-implementations.md)
- [Decodable Implementations](filepath/decodable-implementations.md)
- [Encodable Implementations](filepath/encodable-implementations.md)
- [Equatable Implementations](filepath/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](filepath/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](filepath/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](filepath/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](filepath/hashable-implementations.md)

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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FileDescriptor](filedescriptor.md)
  An abstract handle to an input or output data resource, such as a file or a socket.
- [struct FilePermissions](filepermissions.md)
  The access permissions for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filepath)*