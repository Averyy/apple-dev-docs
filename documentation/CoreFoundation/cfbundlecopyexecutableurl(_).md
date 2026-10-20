# CFBundleCopyExecutableURL(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the location of a bundle’s main executable code.

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
func CFBundleCopyExecutableURL(_ bundle: CFBundle!) -> CFURL!
```

```c
extern CFURLRefCFBundleCopyExecutableURL(CFBundleRef bundle);
```

#### Return Value

A CFURL object describing the location of `bundle`’s executable code, or `NULL` if none is found. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `bundle`: The bundle to examine.

## See Also

### Finding Locations in a Bundle
- [func CFBundleCopyAuxiliaryExecutableURL(CFBundle!, CFString!) -> CFURL!](./cfbundlecopyauxiliaryexecutableurl%28_,_%29.md)
  Returns the location of a bundle’s auxiliary executable code.
- [func CFBundleCopyBuiltInPlugInsURL(CFBundle!) -> CFURL!](./cfbundlecopybuiltinpluginsurl%28_%29.md)
  Returns the location of a bundle’s built in plug-in.
- [func CFBundleCopyPrivateFrameworksURL(CFBundle!) -> CFURL!](./cfbundlecopyprivateframeworksurl%28_%29.md)
  Returns the location of a bundle’s private Frameworks directory.
- [func CFBundleCopyResourcesDirectoryURL(CFBundle!) -> CFURL!](./cfbundlecopyresourcesdirectoryurl%28_%29.md)
  Returns the location of a bundle’s Resources directory.
- [func CFBundleCopySharedFrameworksURL(CFBundle!) -> CFURL!](./cfbundlecopysharedframeworksurl%28_%29.md)
  Returns the location of a bundle’s shared frameworks directory.
- [func CFBundleCopySharedSupportURL(CFBundle!) -> CFURL!](./cfbundlecopysharedsupporturl%28_%29.md)
  Returns the location of a bundle’s shared support files directory.
- [func CFBundleCopySupportFilesDirectoryURL(CFBundle!) -> CFURL!](./cfbundlecopysupportfilesdirectoryurl%28_%29.md)
  Returns the location of the bundle’s support files directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyexecutableurl(_:))*