# earliestPermittedSampleDate()

**Framework**: HealthKit  
**Kind**: method

Returns the earliest date permitted for samples.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func earliestPermittedSampleDate() -> Date
```

## Mentions

- [About the HealthKit framework](about-the-healthkit-framework.md)

#### Return Value

The earliest date that samples can use. You cannot save or query samples prior to this date.

#### Discussion

Attempts to save samples earlier than this date fail with an [`HKError.Code.errorInvalidArgument`](hkerror/code/errorinvalidargument.md) error. Attempts to query samples before this date return samples after this date.

## See Also

- [func delete(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/delete(_:withcompletion:)-78l1m.md)
  Deletes the specified object from the HealthKit store.
- [func delete([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/delete(_:withcompletion:)-17hzm.md)
  Deletes the specified objects from the HealthKit store.
- [func deleteObjects(of: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, (any Error)?) -> Void)](hkhealthstore/deleteobjects(of:predicate:withcompletion:).md)
  Deletes objects saved by this application that match the provided type and predicate.
- [func save(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/save(_:withcompletion:)-6fmtg.md)
  Saves the provided object to the HealthKit store.
- [func save([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/save(_:withcompletion:)-47iwb.md)
  Saves an array of objects to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/earliestpermittedsampledate())*