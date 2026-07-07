# buildEither(first:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Builds an accessory message from the first branch of a conditional.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static func buildEither(first component: AccessoryMessage) -> AccessoryMessage
```

## Parameters

- `component`: An accessory message from the first branch.

## See Also

- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(second:).md)
  Builds an accessory message from the second branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](accessorymessage/builder/buildexpression(_:).md)
  Builds an accessory message from a payload expression.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](accessorymessage/builder/buildoptional(_:).md)
  Builds an accessory message from an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildeither(first:))*