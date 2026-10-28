# startDate

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The start date of the timed metadata.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var startDate: Date? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) NSDate * startDate;
```

## Discussion

The value is `nil` if the metadata item doesn’t provide a start date.

## See Also

### Accessing timing
- [var time: CMTime](./time.md)
  The timestamp for a mutable metadata item.
- [var duration: CMTime](./duration.md)
  The duration of a mutable metadata item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablemetadataitem/startdate)*