# signals

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The set of signals to activate.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var signals: INCarSignalOptions { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INCarSignalOptions signals;
```

*macOS*

```objc
@property (atomic, assign, readonly) INCarSignalOptions signals;
```

#### Discussion

For a list of valid signals, see [`INCarSignalOptions`](../incarsignaloptions.md).

When this property contains a valid [`INCarSignalOptions`](../incarsignaloptions.md) set, activate only the specified audible or visual signals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintent/signals)*