# url(forAuxiliaryExecutable:)

**Framework**: Foundation  
**Kind**: method

Returns the file URL of the executable with the specified name in the receiver’s bundle.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func url(forAuxiliaryExecutable executableName: String) -> URL?
```

#### Return Value

The file URL of the executable `executableName` in the receiver’s bundle.

#### Discussion

This method returns the appropriate path for modern application and framework bundles. This method may not return a URL for non-standard bundle formats or for some older bundle formats.

## Parameters

- `executableName`: The name of an executable file.

## See Also

- [var resourceURL: URL?](bundle/resourceurl.md)
  The file URL of the bundle’s subdirectory containing resource files.
- [var executableURL: URL?](bundle/executableurl.md)
  The file URL of the receiver’s executable file.
- [var privateFrameworksURL: URL?](bundle/privateframeworksurl.md)
  The file URL of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksURL: URL?](bundle/sharedframeworksurl.md)
  The file URL of the receiver’s subdirectory containing shared frameworks.
- [var builtInPlugInsURL: URL?](bundle/builtinpluginsurl.md)
  The file URL of the receiver’s subdirectory containing plug-ins.
- [var sharedSupportURL: URL?](bundle/sharedsupporturl.md)
  The file URL of the bundle’s subdirectory containing shared support files.
- [var appStoreReceiptURL: URL?](bundle/appstorereceipturl.md)
  The file URL for the bundle’s App Store receipt.
- [var resourcePath: String?](bundle/resourcepath.md)
  The full pathname of the bundle’s subdirectory containing resources.
- [var executablePath: String?](bundle/executablepath.md)
  The full pathname of the receiver’s executable file.
- [var privateFrameworksPath: String?](bundle/privateframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksPath: String?](bundle/sharedframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing shared frameworks.
- [var builtInPlugInsPath: String?](bundle/builtinpluginspath.md)
  The full pathname of the receiver’s subdirectory containing plug-ins.
- [func path(forAuxiliaryExecutable: String) -> String?](bundle/path(forauxiliaryexecutable:).md)
  Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportPath: String?](bundle/sharedsupportpath.md)
  The full pathname of the bundle’s subdirectory containing shared support files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/url(forauxiliaryexecutable:))*