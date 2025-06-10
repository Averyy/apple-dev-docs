# result(for:)

**Framework**: HealthKit  
**Kind**: method

Returns the user annotated medications given the query descriptor configuration. Returns the empty array if no HKUserAnnotatedMedication objects match.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func result(for healthStore: HKHealthStore) async throws -> [HKUserAnnotatedMedication]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedicationquerydescriptor/result(for:))*