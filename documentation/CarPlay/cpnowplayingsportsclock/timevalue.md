# timeValue

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The time value you specify at initialization.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var timeValue: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval timeValue;
```

## Discussion

This property contains the time value you specify at initialization time. Use this value as a reference for when you initialized the clock object. CarPlay doesn’t change the value in this property.

## See Also

### Getting the clock attributes
- [var countsUp: Bool](./countsup.md)
  A Boolean value that indicates whether the event clock counts up.
- [var isPaused: Bool](./ispaused.md)
  A Boolean value that indicates whether the clock is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpnowplayingsportsclock/timevalue)*