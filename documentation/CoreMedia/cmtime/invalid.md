# invalid

**Framework**: Core Media  
**Kind**: property

A value that represents an invalid time.

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
static let invalid: CMTime
```

#### Discussion

An invalid time has all of its fields set to `0`.

Don’t test a time against this constant using (time == [`invalid`](cmtime/invalid.md)) because there are many times that are also invalid. Use [`CMTIME_IS_INVALID(_:)`](cmtime_is_invalid(_:).md) instead.

## See Also

- [static let zero: CMTime](cmtime/zero.md)
  A value that represents time zero.
- [static let indefinite: CMTime](cmtime/indefinite.md)
  A value that represents an indefinite time.
- [static let negativeInfinity: CMTime](cmtime/negativeinfinity.md)
  A value that represents negative infinity.
- [static let positiveInfinity: CMTime](cmtime/positiveinfinity.md)
  A value that represents positive infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/invalid)*