# airport

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The airport from which a flight departs or arrives.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var airport: INAirport { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) INAirport * airport;
```

*macOS*

```objc
@property (atomic, copy, readonly) INAirport * airport;
```

## See Also

### Getting the Gate Information
- [var terminal: String?](./terminal.md)
  The terminal from which a flight departs or arrives.
- [var gate: String?](./gate.md)
  An identifier for the gate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inairportgate/airport)*