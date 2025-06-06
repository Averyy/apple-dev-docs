# CFBundleCopyResourcesDirectoryURL(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the location of a bundle’s Resources directory.

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
func CFBundleCopyResourcesDirectoryURL(_ bundle: CFBundle!) -> CFURL!
```

#### Return Value

A CFURL object describing the location of `bundle`’s resources directory, or `NULL` if it could not be found. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

In general, you should never need to use this function. Use [`CFBundleCopyResourceURL(_:_:_:_:)`](cfbundlecopyresourceurl(_:_:_:_:).md) and similar functions instead.

## Parameters

- `bundle`: The bundle to examine.

## See Also

- [func CFBundleCopyAuxiliaryExecutableURL(CFBundle!, CFString!) -> CFURL!](cfbundlecopyauxiliaryexecutableurl(_:_:).md)
  Returns the location of a bundle’s auxiliary executable code.
- [func CFBundleCopyBuiltInPlugInsURL(CFBundle!) -> CFURL!](cfbundlecopybuiltinpluginsurl(_:).md)
  Returns the location of a bundle’s built in plug-in.
- [func CFBundleCopyExecutableURL(CFBundle!) -> CFURL!](cfbundlecopyexecutableurl(_:).md)
  Returns the location of a bundle’s main executable code.
- [func CFBundleCopyPrivateFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopyprivateframeworksurl(_:).md)
  Returns the location of a bundle’s private Frameworks directory.
- [func CFBundleCopySharedFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopysharedframeworksurl(_:).md)
  Returns the location of a bundle’s shared frameworks directory.
- [func CFBundleCopySharedSupportURL(CFBundle!) -> CFURL!](cfbundlecopysharedsupporturl(_:).md)
  Returns the location of a bundle’s shared support files directory.
- [func CFBundleCopySupportFilesDirectoryURL(CFBundle!) -> CFURL!](cfbundlecopysupportfilesdirectoryurl(_:).md)
  Returns the location of the bundle’s support files directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyresourcesdirectoryurl(_:))*