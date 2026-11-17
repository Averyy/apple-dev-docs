# contentType

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a content type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var contentType: some AppSchemaEnum { get }
```

## Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `books` domain and a parameter type matches the `contentType` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum(schema: .books.contentType)` Swift macro.

The following example shows an app enum that conforms to the `contentType` schema. You can create a type that conforms to the schema by adding the `@AppEnum` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `books_contentType` and select it from the code-completion suggestions:

```swift
@AppEnum(schema: .books.contentType)
enum BookContentType: String {
    case <#BookContentType Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [Getting started with the App Intents framework](../../getting-started-with-the-app-intents-framework.md).

## See Also

### Types for static parameters
- [var font: some AppSchemaEnum](./font.md)
  An enum schema for a font.
- [var fontSize: some AppSchemaEnum](./fontsize.md)
  An enum schema for a font size.
- [var navigationDirection: some AppSchemaEnum](./navigationdirection.md)
  An enum schema for a navigation direction.
- [var pageNavigationSetting: some AppSchemaEnum](./pagenavigationsetting.md)
  An enum schema for a page navigation setting.
- [var relativeCharacterSpacingChange: some AppSchemaEnum](./relativecharacterspacingchange.md)
  An enum schema for a relative character spacing change.
- [var relativeFontChange: some AppSchemaEnum](./relativefontchange.md)
  An enum schema for a relative font change.
- [var relativeLineSpacingChange: some AppSchemaEnum](./relativelinespacingchange.md)
  An enum schema for a relative line spacing change.
- [var relativeWordSpacingChange: some AppSchemaEnum](./relativewordspacingchange.md)
  An enum schema for a relative word spacing change.
- [var theme: some AppSchemaEnum](./theme.md)
  An enum schema for a theme.
- [AppSchema.BooksEnum](../booksenum.md)
  Identifies enum schemas in the books domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/booksenum/contenttype)*