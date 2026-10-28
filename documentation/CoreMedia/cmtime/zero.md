# zero

**Framework**: Core Media  
**Kind**: property  
**Role**: Type Property

A value that represents time zero.

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
static let zero: CMTime
```

```c
extern const CMTime kCMTimeZero;
```

## Discussion

Don’t test a time against this constant using (time == [`zero`](./zero.md)) because there are many times that are also `0`. Use [`CMTimeCompare(_:_:)`](../cmtimecompare%28_,_%29.md) instead.

## See Also

### Constants
- [static let invalid: CMTime](./invalid.md)
  A value that represents an invalid time.
- [static let indefinite: CMTime](./indefinite.md)
  A value that represents an indefinite time.
- [static let negativeInfinity: CMTime](./negativeinfinity.md)
  A value that represents negative infinity.
- [static let positiveInfinity: CMTime](./positiveinfinity.md)
  A value that represents positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/zero)*