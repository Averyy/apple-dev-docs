# sampleHasDependentSamples

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether the sample has dependent samples.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var sampleHasDependentSamples: ObjCBool
```

#### Discussion

This value indicates the sample has dependent samples when [`sampleIndicatesWhetherItHasDependentSamples`](avsamplecursordependencyinfo/sampleindicateswhetherithasdependentsamples.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var sampleIndicatesWhetherItHasDependentSamples: ObjCBool](avsamplecursordependencyinfo/sampleindicateswhetherithasdependentsamples.md)
  A Boolean value that determines whether the sample indicates if other samples depend on it.
- [var sampleIndicatesWhetherItDependsOnOthers: ObjCBool](avsamplecursordependencyinfo/sampleindicateswhetheritdependsonothers.md)
  A Boolean value that determines whether the sample indicates that it depends on other samples.
- [var sampleDependsOnOthers: ObjCBool](avsamplecursordependencyinfo/sampledependsonothers.md)
  A Boolean value that determines whether the sample depends on other samples.
- [var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool](avsamplecursordependencyinfo/sampleindicateswhetherithasredundantcoding.md)
  A Boolean value that determines whether the sample indicates that it has redundant coding.
- [var sampleHasRedundantCoding: ObjCBool](avsamplecursordependencyinfo/samplehasredundantcoding.md)
  A Boolean value that determines whether the sample has redundant coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/samplehasdependentsamples)*