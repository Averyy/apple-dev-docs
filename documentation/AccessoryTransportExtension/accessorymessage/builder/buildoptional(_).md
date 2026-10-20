# buildOptional(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Type Method

Builds an accessory message from an optional component.

**Availability**:
- iOS 26.5+

## Declaration

```swift
static func buildOptional(_ component: AccessoryMessage?) -> AccessoryMessage
```

## Parameters

- `component`: An optional accessory message.

## See Also

### Type Methods - generated
- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](./buildeither%28first%29.md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](./buildeither%28second%29.md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](./buildexpression%28_%29.md)
  Builds an accessory message from a payload expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildoptional(_:))*