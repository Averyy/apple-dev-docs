# buildExpression(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Builds an accessory message from a payload expression.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static func buildExpression(_ expression: AccessoryMessage.Payload) -> AccessoryMessage
```

## Parameters

- `expression`: A payload to include in the message.

## See Also

- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(first:).md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(second:).md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](accessorymessage/builder/buildoptional(_:).md)
  Builds an accessory message from an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildexpression(_:))*