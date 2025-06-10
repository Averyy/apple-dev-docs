# UIAccessibilityTextualContext

**Framework**: UIKit  
**Kind**: struct

Constants that describe a named context that helps identify and classify the type of text inside an element.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct UIAccessibilityTextualContext
```

## Topics

### Constants
- [static let console: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/console.md)
  A constant that indicates the text appears in a console context.
- [static let fileSystem: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/filesystem.md)
  A constant that indicates the text appears in a file-system context.
- [static let messaging: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/messaging.md)
  A constant that indicates the text appears in a messaging context.
- [static let narrative: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/narrative.md)
  A constant that indicates the text appears in a narrative speech context.
- [static let sourceCode: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/sourcecode.md)
  A constant that indicates the text appears in a source-code context.
- [static let spreadsheet: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/spreadsheet.md)
  A constant that indicates the text appears in a spreadsheet context.
- [static let wordProcessing: UIAccessibilityTextualContext](uiaccessibilitytextualcontext/wordprocessing.md)
  A constant that indicates the text appears in a word-processing context.
### Initializers
- [init(String)](uiaccessibilitytextualcontext/init(_:).md)
  Creates a textual context.
- [init(rawValue: String)](uiaccessibilitytextualcontext/init(rawvalue:).md)
  Creates a textual context with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIAccessibilityFocus](../ObjectiveC/uiaccessibilityfocus.md)
  An informal protocol that provides a way to determine whether an assistive app, such as VoiceOver, has focus on an accessible element.
- [protocol UIAccessibilityIdentification](uiaccessibilityidentification.md)
  Methods that associate a unique identifier with elements in your user interface.
- [protocol UIAccessibilityReadingContent](uiaccessibilityreadingcontent.md)
  Methods to implement for an object that represents content that users read, such as a book or an article.
- [protocol UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)
  Methods to determine when to adjust images for different content size categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilitytextualcontext)*