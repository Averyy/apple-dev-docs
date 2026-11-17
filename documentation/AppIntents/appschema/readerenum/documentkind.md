# documentKind

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property

An enum schema for a document kind.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var documentKind: some AppSchemaEnum { get }
```

## Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](../../appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `reader` domain and a parameter type matches the `documentKind` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum(schema: .reader.documentKind)` Swift macro.

The following example shows an app enum that conforms to the `documentKind` schema. You can create a type that conforms to the schema by adding the `@AppEnum` macro above the type’s declaration. Xcode inserts a template type into your code for you, which includes the macro, when you type the first few characters of `reader_documentKind` and select it from the code-completion suggestions:

```swift
@AppEnum(schema: .reader.documentKind)
enum ReaderDocumentKind: String {
    case <#ReaderDocumentKind Case#>

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
- [AppSchema.ReaderEnum](../readerenum.md)
  Identifies enum schemas in the reader domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/readerenum/documentkind)*