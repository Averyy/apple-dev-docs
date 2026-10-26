# tip

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The tip for the driver.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var tip: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * tip;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * tip;
```

## See Also

### Identifying the Feedback
- [var rating: NSNumber?](./rating.md)
  The user-supplied rating for the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintent/tip)*