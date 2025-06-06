# save(_:withCompletion:)

**Framework**: HealthKit  
**Kind**: method

Saves an array of objects to the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func save(_ objects: [HKObject]) async throws
```

#### Discussion

This method operates asynchronously. As soon as the save operation is finished, it calls the completion block on a background queue.

If your app has not requested permission to share the object’s data type, the method fails with an [`HKError.Code.errorAuthorizationNotDetermined`](hkerror/code/errorauthorizationnotdetermined.md) error. If your app has been denied permission to save the object’s data type, it fails with an [`HKError.Code.errorAuthorizationDenied`](hkerror/code/errorauthorizationdenied.md) error. Saving an object with the same unique identifier as an object already in the HealthKit store fails with an [`HKError.Code.errorInvalidArgument`](hkerror/code/errorinvalidargument.md) error. When saving multiple objects, if any object cannot be saved, none of them are saved.

In iOS 9.0 and later, saving an object to the HealthKit store sets the object’s [`sourceRevision`](hkobject/sourcerevision.md) property to a [`HKSourceRevision`](hksourcerevision.md) instance representing the saving app. On earlier versions of iOS, saving an object sets the [`source`](hkobject/source.md) property to a [`HKSource`](hksource.md) instance instead. In both cases, these values are available only after the object is retrieved from the HealthKit store. The original object is not changed.

All samples retrieved by iOS 9.0 and later are given a valid [`sourceRevision`](hkobject/sourcerevision.md) property. If the sample was saved using an earlier version of iOS, the source revision’s version is set to `nil`.

## Parameters

- `objects`: An array containing concrete subclasses of the    class (any of the  ,  ,  , or   classes).
- `completion`: A block that this method calls as soon as the save operation is complete. This block is passed the following parameters:

## See Also

- [func delete(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/delete(_:withcompletion:)-78l1m.md)
  Deletes the specified object from the HealthKit store.
- [func delete([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/delete(_:withcompletion:)-17hzm.md)
  Deletes the specified objects from the HealthKit store.
- [func deleteObjects(of: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, (any Error)?) -> Void)](hkhealthstore/deleteobjects(of:predicate:withcompletion:).md)
  Deletes objects saved by this application that match the provided type and predicate.
- [func earliestPermittedSampleDate() -> Date](hkhealthstore/earliestpermittedsampledate.md)
  Returns the earliest date permitted for samples.
- [func save(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](hkhealthstore/save(_:withcompletion:)-6fmtg.md)
  Saves the provided object to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/save(_:withcompletion:)-47iwb)*