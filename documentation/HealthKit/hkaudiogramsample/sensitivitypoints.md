# sensitivityPoints

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

An array of sensitivity point objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var sensitivityPoints: [HKAudiogramSensitivityPoint] { get }
```

```objc
@property (copy, readonly) NSArray<HKAudiogramSensitivityPoint *> * sensitivityPoints;
```

#### Discussion

Each sensitivity point represents a single result from a hearing test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample/sensitivitypoints)*