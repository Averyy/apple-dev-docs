# duration

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The duration of the sample.

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
var duration: CMTime
```

```c
CMTime duration;
```

#### Discussion

If a single struct applies to each of the samples, they all have this duration.

## See Also

### Properties
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The time at which the sample will be decoded.
- [var presentationTimeStamp: CMTime](./presentationtimestamp.md)
  The time at which the sample will be presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampletiminginfo/duration)*