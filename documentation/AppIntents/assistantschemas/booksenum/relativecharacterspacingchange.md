# relativeCharacterSpacingChange

**Framework**: App Intents  
**Kind**: property

The relative change in character spacing for rendering a book.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var relativeCharacterSpacingChange: some AssistantSchemas.Enum { get }
```

#### Overview

Use Swift macros that generate additional properties and add protocol conformance for your app enum implementation. The following example shows an app enum that conforms to the `.books.relativeCharacterSpacingChange` schema:

```swift
@AppEnum(schema: .books.relativeCharacterSpacingChange)
enum BookRelativeCharacterSpacingChange: AppEnum {
    case reset

    static var caseDisplayRepresentations: [BookRelativeCharacterSpacingChange: AppIntents.DisplayRepresentation] = [
        .reset: "Reset"
    ]
}
```

For more information about the `.books` app intent domain, see [`Making ebook actions available to Siri and Apple Intelligence`](making-ebook-actions-available-to-siri-and-apple-intelligence.md). For general information about app intent domains, see [`Integrating actions with Siri and Apple Intelligence`](integrating-actions-with-siri-and-apple-intelligence.md).

## See Also

- [var contentType: some AssistantSchemas.Enum](assistantschemas/booksenum/contenttype.md)
  The content type.
- [var font: some AssistantSchemas.Enum](assistantschemas/booksenum/font.md)
  The font for rendering a book.
- [var fontSize: some AssistantSchemas.Enum](assistantschemas/booksenum/fontsize.md)
  The font size for rendering a book.
- [var navigationDirection: some AssistantSchemas.Enum](assistantschemas/booksenum/navigationdirection.md)
  The navigation direction of a book.
- [var relativeFontChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativefontchange.md)
  The relative change of the font for rendering a book.
- [var relativeLineSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativelinespacingchange.md)
  The relative change in line spacing for rendering a book.
- [var relativeWordSpacingChange: some AssistantSchemas.Enum](assistantschemas/booksenum/relativewordspacingchange.md)
  The relative change in word spacing for rendering a book.
- [var theme: some AssistantSchemas.Enum](assistantschemas/booksenum/theme.md)
  The theme for rendering a book.
- [var pageNavigationSetting: some AssistantSchemas.Enum](assistantschemas/booksenum/pagenavigationsetting.md)
  Navigation settings for rendering a book.
- [AssistantSchemas.BooksEnum](assistantschemas/booksenum.md)
  Assistant schema conformance for types you use to describe ebooks or audiobooks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/assistantschemas/booksenum/relativecharacterspacingchange)*