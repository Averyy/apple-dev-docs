# positiveInfinity

**Framework**: Core Media  
**Kind**: property  
**Role**: Type Property

A value that represents positive infinity.

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
static let positiveInfinity: CMTime
```

```c
extern const CMTime kCMTimePositiveInfinity;
```

#### Discussion

Don’t test a time against this constant using (time == [`positiveInfinity`](./positiveinfinity.md)) because there are many times that are also positive infinity. Use [`CMTIME_IS_POSITIVEINFINITY(_:)`](../cmtime_is_positiveinfinity%28_%29.md) instead.

## See Also

### Constants
- [static let zero: CMTime](./zero.md)
  A value that represents time zero.
- [static let invalid: CMTime](./invalid.md)
  A value that represents an invalid time.
- [static let indefinite: CMTime](./indefinite.md)
  A value that represents an indefinite time.
- [static let negativeInfinity: CMTime](./negativeinfinity.md)
  A value that represents negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/positiveinfinity)*