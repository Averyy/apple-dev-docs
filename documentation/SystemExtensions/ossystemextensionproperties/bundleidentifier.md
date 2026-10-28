# bundleIdentifier

**Framework**: System Extensions  
**Kind**: property  
**Role**: Instance Property

The bundle identifier of the extension.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 10.15+

## Declaration

```swift
var bundleIdentifier: String { get }
```

```objc
@property (strong, readonly) NSString * bundleIdentifier;
```

## Discussion

This is the [`CFBundleIdentifier`](../../BundleResources/information-property-list/cfbundleidentifier.md) of the extension bundle.

## See Also

### Identifying the Extension
- [var bundleVersion: String](./bundleversion.md)
  The bundle version of the extension.
- [var bundleShortVersion: String](./bundleshortversion.md)
  The bundle short version string of the extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemextensions/ossystemextensionproperties/bundleidentifier)*