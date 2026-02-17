# init(_:)

**Framework**: Accessory Transport Extension  
**Kind**: init  
**Required**: Yes

Initializes a feature with a handler factory closure.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
init(_ handlerFactory: @escaping Self.HandlerFactory)
```

## Parameters

- `handlerFactory`: A closure that creates and returns a handler instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature/init(_:))*