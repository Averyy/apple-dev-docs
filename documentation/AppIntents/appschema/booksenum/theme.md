# theme

**Framework**: App Intents  
**Kind**: property

An enum schema for a theme parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var theme: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `books` domain and a parameter type matches the `theme` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .books.theme)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `theme` schema:

```swift
@AppEnum(schema: .books.theme)
enum BookTheme: String {
    case <#BookTheme Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var contentType: some AppSchemaEnum](appschema/booksenum/contenttype.md)
  An enum schema for a content type parameter.
- [var font: some AppSchemaEnum](appschema/booksenum/font.md)
  An enum schema for a font parameter.
- [var fontSize: some AppSchemaEnum](appschema/booksenum/fontsize.md)
  An enum schema for a font size parameter.
- [var navigationDirection: some AppSchemaEnum](appschema/booksenum/navigationdirection.md)
  An enum schema for a navigation direction parameter.
- [var pageNavigationSetting: some AppSchemaEnum](appschema/booksenum/pagenavigationsetting.md)
  An enum schema for a page navigation setting parameter.
- [var relativeCharacterSpacingChange: some AppSchemaEnum](appschema/booksenum/relativecharacterspacingchange.md)
  An enum schema for a relative character spacing change parameter.
- [var relativeFontChange: some AppSchemaEnum](appschema/booksenum/relativefontchange.md)
  An enum schema for a relative font change parameter.
- [var relativeLineSpacingChange: some AppSchemaEnum](appschema/booksenum/relativelinespacingchange.md)
  An enum schema for a relative line spacing change parameter.
- [var relativeWordSpacingChange: some AppSchemaEnum](appschema/booksenum/relativewordspacingchange.md)
  An enum schema for a relative word spacing change parameter.
- [AppSchema.BooksEnum](appschema/booksenum.md)
  Identifies enum schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksenum/theme)*