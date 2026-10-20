# sourceTypes

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The format of the verifiable clinical record.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var sourceTypes: [HKVerifiableClinicalRecordSourceType] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * sourceTypes;
```

#### Discussion

For a list of valid formats, see [`HKVerifiableClinicalRecordSourceType`](../hkverifiableclinicalrecordsourcetype.md).

## See Also

### Accessing the Metadata
- [var recordTypes: [String]](./recordtypes.md)
  The type of records that this query returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquery/sourcetypes)*