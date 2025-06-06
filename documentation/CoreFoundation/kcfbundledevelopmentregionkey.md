# kCFBundleDevelopmentRegionKey

**Framework**: Core Foundation  
**Kind**: var

The name of the development language of the bundle.

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
let kCFBundleDevelopmentRegionKey: CFString!
```

#### Discussion

When CFBundle looks for resources, the fallback is to look in the lproj whose name is given by the `kCFBundleDevelopmentRegionKey` in the `Info.plist` file. You must, therefore, ensure that a bundle contains an lproj with that exact name containing a copy of every localized resource, otherwise CFBundle cannot guarantee the fallback mechanism will work.

## See Also

- [let kCFBundleInfoDictionaryVersionKey: CFString!](kcfbundleinfodictionaryversionkey.md)
  The version of the information property list format.
- [let kCFBundleExecutableKey: CFString!](kcfbundleexecutablekey.md)
  The name of the executable in this bundle (if any).
- [let kCFBundleIdentifierKey: CFString!](kcfbundleidentifierkey.md)
  The bundle identifier.
- [let kCFBundleVersionKey: CFString!](kcfbundleversionkey.md)
  The version number of the bundle.
- [let kCFBundleNameKey: CFString!](kcfbundlenamekey.md)
  The human-readable name of the bundle.
- [let kCFBundleLocalizationsKey: CFString!](kcfbundlelocalizationskey.md)
  Allows an unbundled application that handles localization itself to specify which localizations it has available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfbundledevelopmentregionkey)*