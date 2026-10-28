# handwashingEvent

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A category sample type for handwashing events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let handwashingEvent: HKCategoryTypeIdentifier
```

```c
extern HKCategoryTypeIdentifier const HKCategoryTypeIdentifierHandwashingEvent;
```

## Discussion

Use this type to read or share handwashing events. When creating a handwashing event sample, set the value to [`HKCategoryValue.notApplicable`](../hkcategoryvalue/notapplicable.md), and set the duration by specifying different start and end dates. The Health app uses the sample’s duration to determine if the handwashing event completed.

Apple Watch automatically detects and records handwashing events on Apple Watch Series 4 and later.

## See Also

### Self care
- [static let toothbrushingEvent: HKCategoryTypeIdentifier](./toothbrushingevent.md)
  A category sample type for toothbrushing events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/handwashingevent)*