# CFURLEnumeratorOptions

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

Options for controlling enumerator behavior.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CFURLEnumeratorOptions
```

```c
enum CFURLEnumeratorOptions : CFOptionFlags;
```

## Topics

### Constants
- [static var descendRecursively: CFURLEnumeratorOptions](./cfurlenumeratoroptions/descendrecursively.md)
  The enumerator recurses into each subdirectory enumerated.
- [static var skipInvisibles: CFURLEnumeratorOptions](./cfurlenumeratoroptions/skipinvisibles.md)
  The enumerator skips “hidden” or “invisible” objects.
- [static var generateFileReferenceURLs: CFURLEnumeratorOptions](./cfurlenumeratoroptions/generatefilereferenceurls.md)
  The enumerator generates file reference URLs instead of file path URLs.
- [static var skipPackageContents: CFURLEnumeratorOptions](./cfurlenumeratoroptions/skippackagecontents.md)
  The enumerator skips package directory contents.
- [static var includeDirectoriesPreOrder: CFURLEnumeratorOptions](./cfurlenumeratoroptions/includedirectoriespreorder.md)
  If provided along with the [`descendRecursively`](./cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [static var includeDirectoriesPostOrder: CFURLEnumeratorOptions](./cfurlenumeratoroptions/includedirectoriespostorder.md)
  If provided along with the [`descendRecursively`](./cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.
### Initializers
- [init(rawValue: CFOptionFlags)](./cfurlenumeratoroptions/init%28rawvalue%29.md)
### Type Properties
- [static var generateRelativePathURLs: CFURLEnumeratorOptions](./cfurlenumeratoroptions/generaterelativepathurls.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Enumerations
- [struct CFFileSecurityClearOptions](./cffilesecurityclearoptions.md)
- [struct CFISO8601DateFormatOptions](./cfiso8601dateformatoptions.md)
- [enum CFRunLoopRunResult](./cfrunlooprunresult.md)
- [enum CFURLEnumeratorResult](./cfurlenumeratorresult.md)
  Result codes from the [`CFURLEnumeratorGetNextURL(_:_:_:)`](./cfurlenumeratorgetnexturl%28_,_,_%29.md) function.
- [enum CGRectEdge](./cgrectedge.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions)*