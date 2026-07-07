# buildEither(second:)

**Framework**: Accessory Transport Extension  
**Kind**: method

Builds an accessory message from the second branch of a conditional.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
static func buildEither(second component: AccessoryMessage) -> AccessoryMessage
```

## Parameters

- `component`: An accessory message from the second branch.

## See Also

- [static func buildEither(first: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(first:).md)
  Builds an accessory message from the first branch of a conditional.
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](accessorymessage/builder/buildexpression(_:).md)
  Builds an accessory message from a payload expression.
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](accessorymessage/builder/buildoptional(_:).md)
  Builds an accessory message from an optional component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder/buildeither(second:))*