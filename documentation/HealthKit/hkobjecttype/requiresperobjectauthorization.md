# requiresPerObjectAuthorization()

**Framework**: HealthKit  
**Kind**: method

Returns a Boolean that indicates whether the data type requires per-object authorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func requiresPerObjectAuthorization() -> Bool
```

#### Discussion

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), you must call [`requestPerObjectReadAuthorization(for:predicate:completion:)`](hkhealthstore/requestperobjectreadauthorization(for:predicate:completion:).md) each time you want to query for the data type. The user can then select the individual samples that the app has permission to read. The system always prompts the user for permission, regardless of whether they’ve previously granted permission.

> ❗ **Important**:  Using the [`requestAuthorization(toShare:read:)`](hkhealthstore/requestauthorization(toshare:read:).md) method to request read access to any data types that require per-object authorization fails with an [`HKError.Code.errorInvalidArgument`](hkerror/code/errorinvalidargument.md) error.

## See Also

- [class HKPrescriptionType](hkprescriptiontype.md)
  A type that identifies samples that store a prescription.
- [let HKVisionPrescriptionTypeIdentifier: String](hkvisionprescriptiontypeidentifier.md)
  A type identifier for vision prescription samples.
- [var identifier: String](hkobjecttype/identifier.md)
  A unique string identifying the HealthKit object type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/requiresperobjectauthorization())*