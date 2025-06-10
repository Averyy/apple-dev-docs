# ENRiskScore

**Framework**: Exposure Notification  
**Kind**: typealias

A value signifying the risk of an exposure event.

**Availability**:
- iOS 12.5+
- iPadOS 12.5+
- Mac Catalyst 12.5+

## Declaration

```swift
typealias ENRiskScore = UInt8
```

#### Discussion

> ❗ **Important**:  This type is available in iOS 12.5, and in iOS 13.5 and later.

The risk score incorporates the range and weights of various exposure criteria to produce an estimate of the user’s risk of exposure.

## See Also

- [class ENExposureInfo](enexposureinfo.md)
  The incident information related to a potential exposure.
- [typealias ENRiskLevel](enrisklevel.md)
  The user’s estimated risk of exposure.
- [typealias ENRiskLevelValue](enrisklevelvalue.md)
  The value associated with a particular risk level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enriskscore)*