# AccessoryMessage.Builder

**Framework**: Accessory Transport Extension  
**Kind**: struct

A builder that constructs accessory messages declaratively.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
@resultBuilder
struct Builder
```

## Topics

### Building messages
- [static func buildBlock(AccessoryMessage...) -> AccessoryMessage](accessorymessage/builder/buildblock(_:).md)
  Builds an accessory message from one or more payload components.
### Type Methods - generated
- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(first:).md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(second:).md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](accessorymessage/builder/buildexpression(_:).md)
  Builds an accessory message from a payload expression.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](accessorymessage/builder/buildoptional(_:).md)
  Builds an accessory message from an optional component.

## See Also

- [init(() -> AccessoryMessage)](accessorymessage/init(_:).md)
  Initializes an accessory message using a result builder closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder)*