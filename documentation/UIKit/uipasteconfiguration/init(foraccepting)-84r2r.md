# init(forAccepting:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency convenience init<T>(forAccepting _: T.Type) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## See Also

### Initializing a paste configuration
- [init()](./init%28%29.md)
  Initializes a new paste configuration.
- [convenience init(acceptableTypeIdentifiers: [String])](./init%28acceptabletypeidentifiers%29.md)
  Initializes a new paste configuration with a specified array of acceptable UTIs.
- [convenience init(forAccepting: any NSItemProviderReading.Type)](./init%28foraccepting%29-6is3h.md)
  Initializes a new paste configuration with the UTIs declared as supported by a specified class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(foraccepting:)-84r2r)*