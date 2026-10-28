# sampleHasRedundantCoding

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the sample has redundant coding.

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
var sampleHasRedundantCoding: ObjCBool
```

```c
BOOL sampleHasRedundantCoding;
```

## Discussion

This value indicates the sample has redundant coding when [`sampleIndicatesWhetherItHasRedundantCoding`](./sampleindicateswhetherithasredundantcoding.md) is `true`.

## See Also

### Dependency information
- [var sampleIndicatesWhetherItHasDependentSamples: ObjCBool](./sampleindicateswhetherithasdependentsamples.md)
  A Boolean value that determines whether the sample indicates if other samples depend on it.
- [var sampleHasDependentSamples: ObjCBool](./samplehasdependentsamples.md)
  A Boolean value that determines whether the sample has dependent samples.
- [var sampleIndicatesWhetherItDependsOnOthers: ObjCBool](./sampleindicateswhetheritdependsonothers.md)
  A Boolean value that determines whether the sample indicates that it depends on other samples.
- [var sampleDependsOnOthers: ObjCBool](./sampledependsonothers.md)
  A Boolean value that determines whether the sample depends on other samples.
- [var sampleIndicatesWhetherItHasRedundantCoding: ObjCBool](./sampleindicateswhetherithasredundantcoding.md)
  A Boolean value that determines whether the sample indicates that it has redundant coding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursordependencyinfo/samplehasredundantcoding)*