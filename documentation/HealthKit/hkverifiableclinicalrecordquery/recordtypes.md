# recordTypes

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The type of records that this query returns.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
var recordTypes: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * recordTypes;
```

#### Discussion

For a list of the most common record types, see [`HKVerifiableClinicalRecordCredentialType`](../hkverifiableclinicalrecordcredentialtype.md).

## See Also

### Accessing the Metadata
- [var sourceTypes: [HKVerifiableClinicalRecordSourceType]](./sourcetypes.md)
  The format of the verifiable clinical record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquery/recordtypes)*