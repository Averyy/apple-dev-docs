# bundleVersion

**Framework**: System Extensions  
**Kind**: property  
**Role**: Instance Property

The bundle version of the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
var bundleVersion: String { get }
```

```objc
@property (strong, readonly) NSString * bundleVersion;
```

#### Discussion

This is the [`CFBundleVersion`](../../BundleResources/information-property-list/cfbundleversion.md) of the extension bundle.

## See Also

### Identifying the Extension
- [var bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the extension.
- [var bundleShortVersion: String](./bundleshortversion.md)
  The bundle short version string of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionproperties/bundleversion)*