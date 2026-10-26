# cancellationFeeThreshold

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount of time that must elapse before cancellation fees apply.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var cancellationFeeThreshold: DateComponents? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSDateComponents * cancellationFeeThreshold;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSDateComponents * cancellationFeeThreshold;
```

#### Discussion

Use this property to specify the time after which cancellation fees apply. If cancellation fees apply immediately after booking, set this property to `nil`. The default value of this property is `nil`.

## See Also

### Specifying Cancellation Fees
- [var cancellationFee: INCurrencyAmount?](./cancellationfee.md)
  The cancellation fee charged by your service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelrideintentresponse/cancellationfeethreshold)*