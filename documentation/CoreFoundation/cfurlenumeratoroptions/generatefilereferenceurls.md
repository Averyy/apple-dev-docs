# generateFileReferenceURLs

**Framework**: Core Foundation  
**Kind**: property

The enumerator generates file reference URLs instead of file path URLs.

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
static var generateFileReferenceURLs: CFURLEnumeratorOptions { get }
```

#### Discussion

This option applies only to volume enumerators.

## See Also

- [static var descendRecursively: CFURLEnumeratorOptions](cfurlenumeratoroptions/descendrecursively.md)
  The enumerator recurses into each subdirectory enumerated.
- [static var skipInvisibles: CFURLEnumeratorOptions](cfurlenumeratoroptions/skipinvisibles.md)
  The enumerator skips “hidden” or “invisible” objects.
- [static var skipPackageContents: CFURLEnumeratorOptions](cfurlenumeratoroptions/skippackagecontents.md)
  The enumerator skips package directory contents.
- [static var includeDirectoriesPreOrder: CFURLEnumeratorOptions](cfurlenumeratoroptions/includedirectoriespreorder.md)
  If provided along with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [static var includeDirectoriesPostOrder: CFURLEnumeratorOptions](cfurlenumeratoroptions/includedirectoriespostorder.md)
  If provided along with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/generatefilereferenceurls)*