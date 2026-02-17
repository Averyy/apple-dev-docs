# init(_:)

**Framework**: Accessory Transport Extension  
**Kind**: init

Initializes an accessory message using a result builder closure.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

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