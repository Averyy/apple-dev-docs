# ActivityAuthorizationInfo.ActivityEnablementUpdates

**Framework**: ActivityKit  
**Kind**: struct

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
- [func makeAsyncIterator() -> ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator](activityauthorizationinfo/activityenablementupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator](activityauthorizationinfo/activityenablementupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.Element](activityauthorizationinfo/activityenablementupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.
### Type Aliases
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.AsyncIterator](activityauthorizationinfo/activityenablementupdates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](activityauthorizationinfo/activityenablementupdates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var areActivitiesEnabled: Bool](activityauthorizationinfo/areactivitiesenabled.md)
  A Boolean value that indicates whether your app can start a Live Activity.
- [let activityEnablementUpdates: ActivityAuthorizationInfo.ActivityEnablementUpdates](activityauthorizationinfo/activityenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [init()](activityauthorizationinfo/init.md)
  Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct)*