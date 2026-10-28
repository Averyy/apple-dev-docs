# isArchived

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a medication is archived.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var isArchived: Bool { get }
```

```objc
@property (nonatomic, assign, readonly) BOOL isArchived;
```

## Discussion

The value is `true` if a person moves a medication to the archived section in the Health App. The value is `false` if a medication isn’t in the archived section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkuserannotatedmedication/isarchived)*