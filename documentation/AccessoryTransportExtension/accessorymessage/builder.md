# AccessoryMessage.Builder

**Framework**: Accessory Transport Extension  
**Kind**: struct  
**Role**: Structure

A builder that constructs accessory messages declaratively.

**Availability**:
- iOS 26.5+

## Declaration

```swift
@resultBuilder
struct Builder
```

## Topics

### Building messages
- [static func buildBlock(AccessoryMessage...) -> AccessoryMessage](./builder/buildblock%28_%29.md)
  Builds an accessory message from one or more payload components.
### Type Methods - generated
- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](./builder/buildeither%28first%29.md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](./builder/buildeither%28second%29.md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](./builder/buildexpression%28_%29.md)
  Builds an accessory message from a payload expression.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](./builder/buildoptional%28_%29.md)
  Builds an accessory message from an optional component.

## See Also

### Creating messages
- [init(() -> AccessoryMessage)](./init%28_%29.md)
  Initializes an accessory message using a result builder closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder)*