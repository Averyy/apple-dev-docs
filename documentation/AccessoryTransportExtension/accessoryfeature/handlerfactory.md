# AccessoryFeature.HandlerFactory

**Framework**: Accessory Transport Extension  
**Kind**: typealias

A type alias for a factory closure that creates feature handlers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
typealias HandlerFactory = @Sendable () -> Self.Handler
```

## See Also

- [associatedtype Handler](accessoryfeature/handler.md)
  An associated type that defines the handler for this feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeature/handlerfactory)*