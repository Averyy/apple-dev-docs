# CFURLEnumeratorOptions

**Framework**: Core Foundation  
**Kind**: struct

Options for controlling enumerator behavior.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFURLEnumeratorOptions
```

## Topics

### Constants
- [static var descendRecursively: CFURLEnumeratorOptions](cfurlenumeratoroptions/descendrecursively.md)
  The enumerator recurses into each subdirectory enumerated.
- [static var skipInvisibles: CFURLEnumeratorOptions](cfurlenumeratoroptions/skipinvisibles.md)
  The enumerator skips “hidden” or “invisible” objects.
- [static var generateFileReferenceURLs: CFURLEnumeratorOptions](cfurlenumeratoroptions/generatefilereferenceurls.md)
  The enumerator generates file reference URLs instead of file path URLs.
- [static var skipPackageContents: CFURLEnumeratorOptions](cfurlenumeratoroptions/skippackagecontents.md)
  The enumerator skips package directory contents.
- [static var includeDirectoriesPreOrder: CFURLEnumeratorOptions](cfurlenumeratoroptions/includedirectoriespreorder.md)
  If provided along with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [static var includeDirectoriesPostOrder: CFURLEnumeratorOptions](cfurlenumeratoroptions/includedirectoriespostorder.md)
  If provided along with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.
### Initializers
- [init(rawValue: CFOptionFlags)](cfurlenumeratoroptions/init(rawvalue:).md)
### Type Properties
- [static var generateRelativePathURLs: CFURLEnumeratorOptions](cfurlenumeratoroptions/generaterelativepathurls.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct CFFileSecurityClearOptions](cffilesecurityclearoptions.md)
- [struct CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [enum CFRunLoopRunResult](cfrunlooprunresult.md)
- [enum CFURLEnumeratorResult](cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](cfurlenumeratorgetnexturl(_:_:_:).md) function.
- [enum CGRectEdge](cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions)*