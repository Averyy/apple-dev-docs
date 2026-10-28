# decodeTimeStamp

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The time at which the sample will be decoded.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var decodeTimeStamp: CMTime
```

```c
CMTime decodeTimeStamp;
```

## Discussion

If the samples are in presentation order, this must be set to `kCMTimeInvalid`.

## See Also

### Properties
- [var duration: CMTime](./duration.md)
  The duration of the sample.
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The time at which the sample will be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampletiminginfo/decodetimestamp)*