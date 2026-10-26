# NSTextScalingType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify the text scaling.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum NSTextScalingType
```

```c
enum NSTextScalingType : NSInteger;
```

## Topics

### Constants
- [NSTextScalingType.standard](./nstextscalingtype/standard.md)
  Font sizes throughout the document appear visually similar to how they would render in macOS and non-Apple platforms.
- [NSTextScalingType.iOS](./nstextscalingtype/ios.md)
  Font sizes throughout the document appear visually similar to how they would render in iOS.
### Initializers
- [init?(rawValue: Int)](./nstextscalingtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Related Documentation
- [static let textScaling: NSAttributedString.DocumentAttributeKey](../Foundation/nsattributedstring/documentattributekey/textscaling.md)
  The text-scaling mode to use when displaying the text.
- [static let sourceTextScaling: NSAttributedString.DocumentAttributeKey](../Foundation/nsattributedstring/documentattributekey/sourcetextscaling.md)
  The text-scaling mode you used when creating the text.
- [static let targetTextScaling: NSAttributedString.DocumentReadingOptionKey](../Foundation/nsattributedstring/documentreadingoptionkey/targettextscaling.md)
  The text scaling mode to use after reading the text from disk.
- [static let sourceTextScaling: NSAttributedString.DocumentReadingOptionKey](../Foundation/nsattributedstring/documentreadingoptionkey/sourcetextscaling.md)
  The text-scaling mode to associate with the document’s content.
### Getting document-wide attributes
- [NSAttributedStringDocumentAttributeKey](./nsattributedstringdocumentattributekey.md)
  The attributes you apply to an entire document.
- [Document reading option keys](./document-reading-option-keys.md)
  Keys for constructing an attributed string from data on disk.
- [NSAttributedStringDocumentType](./nsattributedstringdocumenttype.md)
  Constants for the document type document attribute key.
- [NSTextLayoutSectionKey](./nstextlayoutsectionkey.md)
  Constants for the text layout sections document attribute key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextscalingtype)*