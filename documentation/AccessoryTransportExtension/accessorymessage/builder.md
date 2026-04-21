# AccessoryMessage.Builder

**Framework**: Accessory Transport Extension  
**Kind**: struct

A builder that constructs accessory messages declaratively.

**Availability**:
- iOS 26.5+ (Beta)
- iPadOS 26.5+ (Beta)
- Mac Catalyst 26.5+ (Beta)

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
- [static func buildEither(second: AccessoryMessage) -> AccessoryMessage](accessorymessage/builder/buildeither(second:).md)
- [static func buildExpression(AccessoryMessage.Payload) -> AccessoryMessage](accessorymessage/builder/buildexpression(_:).md)
- [static func buildOptional(AccessoryMessage?) -> AccessoryMessage](accessorymessage/builder/buildoptional(_:).md)

## See Also

- [init(() -> AccessoryMessage)](accessorymessage/init(_:).md)
  Initializes an accessory message using a result builder closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder)*