# referenceSex

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The sex whose reference ranges should be used when classifying a clinical measurement for this user.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
var referenceSex: HKReferenceSex { get throws }
```

## Discussion

`.notSet` when the user has not provided a value. Throws if read authorization was not granted or the value could not be read.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/referencesex)*