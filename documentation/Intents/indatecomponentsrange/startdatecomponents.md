# startDateComponents

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The start date of the range.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var startDateComponents: DateComponents? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSDateComponents * startDateComponents;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSDateComponents * startDateComponents;
```

#### Discussion

The contents of this property are set at initialization time and cannot be changed later. If the value of this property is `nil`, the start time is in the distant past.

## See Also

### Getting the Date Information
- [var endDateComponents: DateComponents?](./enddatecomponents.md)
  The end date of the range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatecomponentsrange/startdatecomponents)*