# buildExpression(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

Builds an accessory message from a payload expression.

**Availability**:
- iOS 26.5+

## Declaration

```swift
static func buildExpression(_ expression: AccessoryMessage.Payload) -> AccessoryMessage
```

## Parameters

- `expression`: A payload to include in the message.

## See Also

### Type Methods - generated
- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](./buildeither%28first%29.md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](./buildeither%28second%29.md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](./buildoptional%28_%29.md)
  Builds an accessory message from an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildexpression(_:))*