# indefinite

**Framework**: Core Media  
**Kind**: property  
**Role**: Type Property

A value that represents an indefinite time.

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
static let indefinite: CMTime
```

```c
extern const CMTime kCMTimeIndefinite;
```

## Discussion

Don’t test a time against this constant using (`time ==` [`indefinite`](./indefinite.md)) because there are many that are also indefinite. Use [`CMTIME_IS_INDEFINITE(_:)`](../cmtime_is_indefinite%28_%29.md) instead.

## See Also

### Constants
- [static let zero: CMTime](./zero.md)
  A value that represents time zero.
- [static let invalid: CMTime](./invalid.md)
  A value that represents an invalid time.
- [static let negativeInfinity: CMTime](./negativeinfinity.md)
  A value that represents negative infinity.
- [static let positiveInfinity: CMTime](./positiveinfinity.md)
  A value that represents positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/indefinite)*