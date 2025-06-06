# electrocardiogramType()

**Framework**: Healthkit  
**Kind**: method

Returns the shared electrocardiogram type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func electrocardiogramType() -> HKElectrocardiogramType
```

#### Return Value

The shared [`HKElectrocardiogramType`](hkelectrocardiogramtype.md) instance.

#### Discussion

This method returns an instance of the [`HKElectrocardiogramType`](hkelectrocardiogramtype.md) concrete subclass. Use this type to request permission to read [`HKElectrocardiogram`](hkelectrocardiogram.md) objects from the HealthKit store.

> **Note**:  You can’t request permission to share [`HKActivitySummary`](hkactivitysummary.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/electrocardiogramtype())*