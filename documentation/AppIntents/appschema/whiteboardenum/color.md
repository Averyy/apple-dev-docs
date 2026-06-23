# color

**Framework**: App Intents  
**Kind**: property

An enum schema for a color parameter.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var color: some AppSchemaEnum { get }
```

#### Discussion

To make your app’s parameter types available to Apple Intelligence, conform your [`AppEnum`](appenum.md) to a schema that describes a parameter’s possible values to the system. If your app’s functionality aligns with the `whiteboard` domain and a parameter type matches the `color` schema, you can generate the protocol conformance the schema requires for your app enum implementation with the `@AppEnum( .whiteboard.color)` Swift macro. To make your app work with Siri, see [`Apple Intelligence and Siri AI`](apple-intelligence-and-siri-ai.md).

The following example shows an app enum that conforms to the `color` schema:

```swift
@AppEnum(schema: .whiteboard.color)
enum CanvasColor: String {
    case <#CanvasColor Case#>

    static let caseDisplayRepresentations: [Self: DisplayRepresentation] = [
        <#DisplayRepresentations#>
    ]
}
```

The schema supports the following system experiences:

- Shortcuts

For more information about the App Intents framework and the experiences it supports, see [`Getting started with the App Intents framework`](getting-started-with-the-app-intents-framework.md).

## See Also

- [var itemType: some AppSchemaEnum](appschema/whiteboardenum/itemtype.md)
  An enum schema for an item type parameter.
- [AppSchema.WhiteboardEnum](appschema/whiteboardenum.md)
  Identifies enum schemas in the whiteboard domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appschema/whiteboardenum/color)*