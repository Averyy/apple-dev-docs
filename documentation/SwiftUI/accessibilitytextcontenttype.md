# AccessibilityTextContentType

**Framework**: SwiftUI  
**Kind**: struct

Textual context that assistive technologies can use to improve the presentation of spoken text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct AccessibilityTextContentType
```

#### Overview

Use an `AccessibilityTextContentType` value when setting the accessibility text content type of a view using the [`accessibilityTextContentType(_:)`](view/accessibilitytextcontenttype(_:).md) modifier.

## Topics

### Getting content types
- [static let console: AccessibilityTextContentType](accessibilitytextcontenttype/console.md)
  A type that represents text used for input, like in the Terminal app.
- [static let fileSystem: AccessibilityTextContentType](accessibilitytextcontenttype/filesystem.md)
  A type that represents text used by a file browser, like in the Finder app in macOS.
- [static let messaging: AccessibilityTextContentType](accessibilitytextcontenttype/messaging.md)
  A type that represents text used in a message, like in the Messages app.
- [static let narrative: AccessibilityTextContentType](accessibilitytextcontenttype/narrative.md)
  A type that represents text used in a story or poem, like in the Books app.
- [static let plain: AccessibilityTextContentType](accessibilitytextcontenttype/plain.md)
  A type that represents generic text that has no specific type.
- [static let sourceCode: AccessibilityTextContentType](accessibilitytextcontenttype/sourcecode.md)
  A type that represents text used in source code, like in Swift Playgrounds.
- [static let spreadsheet: AccessibilityTextContentType](accessibilitytextcontenttype/spreadsheet.md)
  A type that represents text used in a grid of data, like in the Numbers app.
- [static let wordProcessing: AccessibilityTextContentType](accessibilitytextcontenttype/wordprocessing.md)
  A type that represents text used in a document, like in the Pages app.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accessibilityTextContentType(AccessibilityTextContentType) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilitytextcontenttype(_:).md)
  Sets an accessibility text content type.
- [func accessibilityHeading(AccessibilityHeadingLevel) -> ModifiedContent<Self, AccessibilityAttachmentModifier>](view/accessibilityheading(_:).md)
  Sets the accessibility level of this heading.
- [enum AccessibilityHeadingLevel](accessibilityheadinglevel.md)
  The hierarchy of a heading in relation to other headings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/accessibilitytextcontenttype)*