# init(_:)

**Framework**: Accessory Transport Extension  
**Kind**: init

Initializes an accessory message using a result builder closure.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
init(@AccessoryMessage.Builder _ builder: () -> AccessoryMessage)
```

## Parameters

- `builder`: A closure that returns an accessory message using the result builder syntax.

## See Also

- [AccessoryMessage.Builder](accessorymessage/builder.md)
  A builder that constructs accessory messages declaratively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorymessage/init(_:))*