# init(numberOfBands:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates an audio unit equalizer object with the specified number of bands.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(numberOfBands: Int)
```

```objc
- (instancetype) initWithNumberOfBands:(NSUInteger) numberOfBands;
```

## Return Value

A new `AVAudioUnitEQ` instance.

## Parameters

- `numberOfBands`: The number of bands that the equalizer creates.

## See Also

### Related Documentation
- [var bands: [AVAudioUnitEQFilterParameters]](./bands.md)
  An array of equalizer filter parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiouniteq/init(numberofbands:))*