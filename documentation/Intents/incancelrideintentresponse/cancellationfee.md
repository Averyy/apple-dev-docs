# cancellationFee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The cancellation fee charged by your service.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var cancellationFee: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * cancellationFee;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * cancellationFee;
```

## Discussion

SiriKit communicates your cancellation fee to the user as part of the confirmation process. Specify a value for the [`cancellationFeeThreshold`](./cancellationfeethreshold.md) property if cancellation fees apply only after a period of time has elapsed.

## See Also

### Specifying Cancellation Fees
- [var cancellationFeeThreshold: DateComponents?](./cancellationfeethreshold.md)
  The amount of time that must elapse before cancellation fees apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponse/cancellationfee)*