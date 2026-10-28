# delete(_:withCompletion:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Deletes the specified object from the HealthKit store.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func delete(_ object: HKObject, withCompletion completion: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

```swift
func delete(_ object: HKObject) async throws
```

```objc
- (void) deleteObject:(HKObject *) object withCompletion:(void (^)(BOOL success, NSError *error)) completion;
```

## Discussion

Your app can delete only those objects that it has previously saved to the HealthKit store. If the user revokes sharing permission, you can no longer delete the object. This method operates asynchronously. As soon as the delete operation is finished, it calls the completion block on a background queue.

If your app has not requested permission to share the object’s data type, the method fails with an [`HKError.Code.errorAuthorizationNotDetermined`](../hkerror/code/errorauthorizationnotdetermined.md) error. If your app has been denied permission to share the object’s data type, it fails with an [`HKError.Code.errorAuthorizationDenied`](../hkerror/code/errorauthorizationdenied.md) error.

HealthKit stores a temporary [`HKDeletedObject`](../hkdeletedobject.md) entry, letting you query for recently deleted objects. However, the deleted objects are periodically removed to save storage space. If you want your app to receive notifications about all the deleted objects, set up an observer query, and enable it for background delivery. In the background query’s update handler, create an [`HKAnchoredObjectQuery`](../hkanchoredobjectquery.md) object to gather the list of recently deleted objects.

> **Note**:  Although your app can manage only the objects it created and saved, users can always delete any data through the Health app.

## Parameters

- `object`: An object that this app has previously saved to the HealthKit store.
- `completion`: A block that this method calls as soon as the delete operation is complete. This block is passed the following parameters:

  - **success**: A Boolean value. This parameter contains [`true`](../../Swift/true.md) if the object was successfully deleted; otherwise, [`false`](../../Swift/false.md).
  - **error**: An error object. If an error occurred, this object contains information about the error; otherwise, it is set to `nil`.

## See Also

### Working with HealthKit objects
- [func delete([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](./delete%28_,withcompletion%29-17hzm.md)
  Deletes the specified objects from the HealthKit store.
- [func deleteObjects(of: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, (any Error)?) -> Void)](./deleteobjects%28of,predicate,withcompletion%29.md)
  Deletes objects saved by this application that match the provided type and predicate.
- [func save(HKObject, withCompletion: (Bool, (any Error)?) -> Void)](./save%28_,withcompletion%29-6fmtg.md)
  Saves the provided object to the HealthKit store.
- [func save([HKObject], withCompletion: (Bool, (any Error)?) -> Void)](./save%28_,withcompletion%29-47iwb.md)
  Saves an array of objects to the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/delete(_:withcompletion:)-78l1m)*