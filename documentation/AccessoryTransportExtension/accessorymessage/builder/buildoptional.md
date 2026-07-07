# buildOptional(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Builds an accessory message from an optional component.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static func buildOptional(_ component: AccessoryMessage?) -> AccessoryMessage
```

## Parameters

- `component`: An optional accessory message.

## See Also

- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(first:).md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(second:).md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](accessorymessage/builder/buildexpression(_:).md)
  Builds an accessory message from a payload expression.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildoptional(_:))*