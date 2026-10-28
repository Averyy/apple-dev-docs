# signals

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of signal produced (audible or visual).

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var signals: INCarSignalOptions { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readwrite) INCarSignalOptions signals;
```

*macOS*

```objc
@property (atomic, assign, readwrite) INCarSignalOptions signals;
```

## Discussion

Typically, you assign a value to this property only after handling the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponse/signals)*