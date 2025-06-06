# includeDirectoriesPostOrder

**Framework**: Core Foundation  
**Kind**: property

If provided along with the [`descendRecursively`](cfurlenumeratoroptions/descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.

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
static var includeDirectoriesPostOrder: CFURLEnumeratorOptions { get }
```

#### Discussion

A recursive post-order enumerator returns [`CFURLEnumeratorResult.directoryPostOrderSuccess`](cfurlenumeratorresult/directorypostordersuccess.md) when it returns a directory’s URL after returning the directory’s descendents.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespostorder)*