# descendRecursively

**Framework**: Core Foundation  
**Kind**: property  
**Role**: Type Property

The enumerator recurses into each subdirectory enumerated.

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
static var descendRecursively: CFURLEnumeratorOptions { get }
```

```c
kCFURLEnumeratorDescendRecursively
```

#### Discussion

This option applies only to directory enumerators.

You can enumerate the directories that a recursive enumerator encounters in pre-order fashion, post-order fashion, or both, by providing a combination of the [`includeDirectoriesPreOrder`](./includedirectoriespreorder.md) and [`includeDirectoriesPostOrder`](./includedirectoriespostorder.md) options. If you provide neither option, the recursive enumerator behaves as if it was provided the [`includeDirectoriesPreOrder`](./includedirectoriespreorder.md) option.

## See Also

### Constants
- [static var skipInvisibles: CFURLEnumeratorOptions](./skipinvisibles.md)
  The enumerator skips “hidden” or “invisible” objects.
- [static var generateFileReferenceURLs: CFURLEnumeratorOptions](./generatefilereferenceurls.md)
  The enumerator generates file reference URLs instead of file path URLs.
- [static var skipPackageContents: CFURLEnumeratorOptions](./skippackagecontents.md)
  The enumerator skips package directory contents.
- [static var includeDirectoriesPreOrder: CFURLEnumeratorOptions](./includedirectoriespreorder.md)
  If provided along with the [`descendRecursively`](./descendrecursively.md) option, the recursive enumerator returns a directory’s URL before returning the URLs of the directory’s descendents.
- [static var includeDirectoriesPostOrder: CFURLEnumeratorOptions](./includedirectoriespostorder.md)
  If provided along with the [`descendRecursively`](./descendrecursively.md) option, the recursive enumerator returns a directory’s URL after returning the URLs of the directory’s descendents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlenumeratoroptions/descendrecursively)*