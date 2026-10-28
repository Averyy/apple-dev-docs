# duration

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Instance Property

The duration of the audio you use to generate the signature.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var duration: TimeInterval { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) NSTimeInterval duration;
```

*macOS*

```objc
@property (atomic, assign, readonly) NSTimeInterval duration;
```

## Discussion

Audio that contains periods of silence may result in a duration value that’s shorter than the full duration of the original audio track.

## See Also

### Reading signature information
- [var dataRepresentation: Data](./datarepresentation.md)
  The raw data for the signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/duration)*