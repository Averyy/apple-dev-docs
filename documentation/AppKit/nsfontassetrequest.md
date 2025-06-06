# NSFontAssetRequest

**Framework**: AppKit  
**Kind**: class

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSFontAssetRequest
```

## Topics

### Creating a Font Asset Request
- [init(fontDescriptors: [NSFontDescriptor], options: NSFontAssetRequest.Options)](nsfontassetrequest/init(fontdescriptors:options:).md)
- [NSFontAssetRequest.Options](nsfontassetrequest/options.md)
### Downloading a Font Asset
- [func download(withCompletionHandler: ((any Error)?) -> Bool)](nsfontassetrequest/download(withcompletionhandler:).md)
- [var downloadedFontDescriptors: [NSFontDescriptor]](nsfontassetrequest/downloadedfontdescriptors.md)
### Getting the Download Progress
- [var progress: Progress](nsfontassetrequest/progress.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](../Foundation/ProgressReporting.md)

## See Also

- [class NSFont](nsfont.md)
  The representation of a font in an app.
- [class NSFontDescriptor](nsfontdescriptor.md)
  A dictionary of attributes that describe a font.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontassetrequest)*