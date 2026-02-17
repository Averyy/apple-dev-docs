# AccessoryMessage.Builder

**Framework**: Accessory Transport Extension  
**Kind**: struct

A builder that constructs accessory messages declaratively.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
@resultBuilder
struct Builder
```

## Topics

### Building messages
- [static func buildBlock(AccessoryMessage.Payload...) -> AccessoryMessage](accessorymessage/builder/buildblock(_:).md)
  Builds an accessory message from one or more payload components.

## See Also

- [init(() -> AccessoryMessage)](accessorymessage/init(_:).md)
  Initializes an accessory message using a result builder closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/builder)*