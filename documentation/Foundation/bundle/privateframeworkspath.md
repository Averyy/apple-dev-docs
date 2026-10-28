# privateFrameworksPath

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The full pathname of the bundle’s subdirectory containing private frameworks.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var privateFrameworksPath: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * privateFrameworksPath;
```

## Discussion

This property contains the appropriate path for modern application and framework bundles. This property may not contain a path for non-standard bundle formats or for some older bundle formats.

## See Also

### Getting the standard bundle directories
- [var resourceURL: URL?](./resourceurl.md)
  The file URL of the bundle’s subdirectory containing resource files.
- [var executableURL: URL?](./executableurl.md)
  The file URL of the receiver’s executable file.
- [var privateFrameworksURL: URL?](./privateframeworksurl.md)
  The file URL of the bundle’s subdirectory containing private frameworks.
- [var sharedFrameworksURL: URL?](./sharedframeworksurl.md)
  The file URL of the receiver’s subdirectory containing shared frameworks.
- [var builtInPlugInsURL: URL?](./builtinpluginsurl.md)
  The file URL of the receiver’s subdirectory containing plug-ins.
- [func url(forAuxiliaryExecutable: String) -> URL?](./url%28forauxiliaryexecutable%29.md)
  Returns the file URL of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportURL: URL?](./sharedsupporturl.md)
  The file URL of the bundle’s subdirectory containing shared support files.
- [var appStoreReceiptURL: URL?](./appstorereceipturl.md)
  The file URL for the bundle’s App Store receipt.
- [var resourcePath: String?](./resourcepath.md)
  The full pathname of the bundle’s subdirectory containing resources.
- [var executablePath: String?](./executablepath.md)
  The full pathname of the receiver’s executable file.
- [var sharedFrameworksPath: String?](./sharedframeworkspath.md)
  The full pathname of the bundle’s subdirectory containing shared frameworks.
- [var builtInPlugInsPath: String?](./builtinpluginspath.md)
  The full pathname of the receiver’s subdirectory containing plug-ins.
- [func path(forAuxiliaryExecutable: String) -> String?](./path%28forauxiliaryexecutable%29.md)
  Returns the full pathname of the executable with the specified name in the receiver’s bundle.
- [var sharedSupportPath: String?](./sharedsupportpath.md)
  The full pathname of the bundle’s subdirectory containing shared support files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/privateframeworkspath)*