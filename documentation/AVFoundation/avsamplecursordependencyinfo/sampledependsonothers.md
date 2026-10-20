# sampleDependsOnOthers

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the sample depends on other samples.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var sampleDependsOnOthers: ObjCBool
```

```c
BOOL sampleDependsOnOthers;
```

#### Discussion

This value indicates whether the sample depends on other media samples when [`sampleIndicatesWhetherItDependsOnOthers`](./sampleindicateswhetheritdependsonothers.md) is [`true`](../../Swift/true.md).

## See Also

### Dependency information
- [var sampleIndicatesWhetherItHasDependentSamples: ObjCBool](./sampleindicateswhetherithasdependentsamples.md)
  A Boolean value that determines whether the sample indicates if other samples depend on it.
- [var sampleHasDependentSamples: ObjCBool](./samplehasdependentsamples.md)
  A Boolean value that determines whether the sample has dependent samples.
- [var sampleIndicatesWhetherItDependsOnOthers: ObjCBool](./sampleindicateswhetheritdependsonothers.md)
  A Boolean value that determines whether the sample indicates that it depends on other samples.
- [var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool](./sampleindicateswhetherithasredundantcoding.md)
  A Boolean value that determines whether the sample indicates that it has redundant coding.
- [var sampleHasRedundantCoding: ObjCBool](./samplehasredundantcoding.md)
  A Boolean value that determines whether the sample has redundant coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/sampledependsonothers)*