# presentationTimeStamp

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

The time at which the sample will be presented.

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
var presentationTimeStamp: CMTime
```

```c
CMTime presentationTimeStamp;
```

#### Discussion

If a single struct applies to each of the samples, they all have this duration.

## See Also

### Properties
- [var decodeTimeStamp: CMTime](./decodetimestamp.md)
  The time at which the sample will be decoded.
- [var duration: CMTime](./duration.md)
  The duration of the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsampletiminginfo/presentationtimestamp)*