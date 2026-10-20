# bundleShortVersion

**Framework**: System Extensions  
**Kind**: property  
**Role**: Instance Property

The bundle short version string of the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
var bundleShortVersion: String { get }
```

```objc
@property (strong, readonly) NSString * bundleShortVersion;
```

#### Discussion

This is the [`CFBundleShortVersionString`](../../BundleResources/information-property-list/cfbundleshortversionstring.md) of the extension bundle.

## See Also

### Identifying the Extension
- [var bundleIdentifier: String](./bundleidentifier.md)
  The bundle identifier of the extension.
- [var bundleVersion: String](./bundleversion.md)
  The bundle version of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionproperties/bundleshortversion)*