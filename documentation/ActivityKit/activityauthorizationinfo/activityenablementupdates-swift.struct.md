# ActivityAuthorizationInfo.ActivityEnablementUpdates

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure that offers functionality to observe whether your app can start a Live Activity.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct ActivityEnablementUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator](./activityenablementupdates-swift.struct/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator](./activityenablementupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.Element](./activityenablementupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Observing Live Activity permission changes
- [var areActivitiesEnabled: Bool](./areactivitiesenabled.md)
  A Boolean value that indicates whether your app can start a Live Activity.
- [let activityEnablementUpdates: ActivityAuthorizationInfo.ActivityEnablementUpdates](./activityenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [init()](./init%28%29.md)
  Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct)*