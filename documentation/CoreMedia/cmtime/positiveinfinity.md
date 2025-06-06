# positiveInfinity

**Framework**: Core Media  
**Kind**: property

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

#### Discussion

Don’t test a time against this constant using (time == [`positiveInfinity`](cmtime/positiveinfinity.md)) because there are many times that are also positive infinity. Use [`CMTIME_IS_POSITIVEINFINITY(_:)`](cmtime_is_positiveinfinity(_:).md) instead.

## See Also

- [static let zero: CMTime](cmtime/zero.md)
  A value that represents time zero.
- [static let invalid: CMTime](cmtime/invalid.md)
  A value that represents an invalid time.
- [static let indefinite: CMTime](cmtime/indefinite.md)
  A value that represents an indefinite time.
- [static let negativeInfinity: CMTime](cmtime/negativeinfinity.md)
  A value that represents negative infinity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtime/positiveinfinity)*