# isMinimumDurationRestricted

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether samples of this type have a minimum time interval between the start and end dates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var isMinimumDurationRestricted: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isMinimumDurationRestricted;
```

## See Also

### Checking the Duration Restriction
- [var minimumAllowedDuration: TimeInterval](./minimumallowedduration.md)
  The minimum duration if the sample type has a restricted duration.
- [var isMaximumDurationRestricted: Bool](./ismaximumdurationrestricted.md)
  A Boolean value that indicates whether samples of this type have a maximum time interval between the start and end dates.
- [var maximumAllowedDuration: TimeInterval](./maximumallowedduration.md)
  The maximum duration if the sample type has a restricted duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksampletype/isminimumdurationrestricted)*