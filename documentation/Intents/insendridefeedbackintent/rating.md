# rating

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user-supplied rating for the driver.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var rating: NSNumber? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSNumber * rating;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSNumber * rating;
```

## See Also

### Identifying the Feedback
- [var tip: INCurrencyAmount?](./tip.md)
  The tip for the driver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insendridefeedbackintent/rating)*