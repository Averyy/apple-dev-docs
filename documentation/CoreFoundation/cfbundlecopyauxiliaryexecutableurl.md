# CFBundleCopyAuxiliaryExecutableURL(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the location of a bundle’s auxiliary executable code.

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
func CFBundleCopyAuxiliaryExecutableURL(_ bundle: CFBundle!, _ executableName: CFString!) -> CFURL!
```

#### Return Value

The URL location of the specified bundle’s auxiliary executable code, or `NULL` if it could not be found. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

This function can be used to find executables other than your main executable. This is useful, for instance, for applications that have some command line tool that is packaged with and used by the application. The tool can be packaged in the various platform executable directories in the bundle and can be located with this function. This allows an application to ship versions of the tool for each platform as it does for the main application executable.

## Parameters

- `bundle`: The bundle to examine.
- `executableName`: The name of  ’s auxiliary executable code.

## See Also

- [func CFBundleCopyBuiltInPlugInsURL(CFBundle!) -> CFURL!](cfbundlecopybuiltinpluginsurl(_:).md)
  Returns the location of a bundle’s built in plug-in.
- [func CFBundleCopyExecutableURL(CFBundle!) -> CFURL!](cfbundlecopyexecutableurl(_:).md)
  Returns the location of a bundle’s main executable code.
- [func CFBundleCopyPrivateFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopyprivateframeworksurl(_:).md)
  Returns the location of a bundle’s private Frameworks directory.
- [func CFBundleCopyResourcesDirectoryURL(CFBundle!) -> CFURL!](cfbundlecopyresourcesdirectoryurl(_:).md)
  Returns the location of a bundle’s Resources directory.
- [func CFBundleCopySharedFrameworksURL(CFBundle!) -> CFURL!](cfbundlecopysharedframeworksurl(_:).md)
  Returns the location of a bundle’s shared frameworks directory.
- [func CFBundleCopySharedSupportURL(CFBundle!) -> CFURL!](cfbundlecopysharedsupporturl(_:).md)
  Returns the location of a bundle’s shared support files directory.
- [func CFBundleCopySupportFilesDirectoryURL(CFBundle!) -> CFURL!](cfbundlecopysupportfilesdirectoryurl(_:).md)
  Returns the location of the bundle’s support files directory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlecopyauxiliaryexecutableurl(_:_:))*