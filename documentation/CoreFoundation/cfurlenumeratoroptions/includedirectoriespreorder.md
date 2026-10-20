# includeDirectoriesPreOrder

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

If provided along with the [`descendRecursively`](./descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.

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
static var includeDirectoriesPreOrder: CFURLEnumeratorOptions { get }
```

```c
kCFURLEnumeratorIncludeDirectoriesPreOrder
```

## See Also

### Constants
- [static var descendRecursively: CFURLEnumeratorOptions](./descendrecursively.md)
  The enumerator recurses into each subdirectory enumerated.
- [static var skipInvisibles: CFURLEnumeratorOptions](./skipinvisibles.md)
  The enumerator skips “hidden” or “invisible” objects.
- [static var generateFileReferenceURLs: CFURLEnumeratorOptions](./generatefilereferenceurls.md)
  The enumerator generates file reference URLs instead of file path URLs.
- [static var skipPackageContents: CFURLEnumeratorOptions](./skippackagecontents.md)
  The enumerator skips package directory contents.
- [static var includeDirectoriesPostOrder: CFURLEnumeratorOptions](./includedirectoriespostorder.md)
  If provided along with the [`descendRecursively`](./descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/includedirectoriespreorder)*