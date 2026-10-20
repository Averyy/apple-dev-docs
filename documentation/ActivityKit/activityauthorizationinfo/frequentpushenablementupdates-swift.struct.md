# ActivityAuthorizationInfo.FrequentPushEnablementUpdates

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

A structure that can observe whether you can update Live Activities with frequent ActivityKit push notifications.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
struct FrequentPushEnablementUpdates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> ActivityAuthorizationInfo.FrequentPushEnablementUpdates.Iterator](./frequentpushenablementupdates-swift.struct/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [ActivityAuthorizationInfo.FrequentPushEnablementUpdates.Iterator](./frequentpushenablementupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
- [ActivityAuthorizationInfo.FrequentPushEnablementUpdates.Element](./frequentpushenablementupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)

## See Also

### Observing availability of frequent ActivityKit push notifications
- [var frequentPushesEnabled: Bool](./frequentpushesenabled.md)
  A Boolean value that indicates whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.
- [let frequentPushEnablementUpdates: ActivityAuthorizationInfo.FrequentPushEnablementUpdates](./frequentpushenablementupdates-swift.property.md)
  An asynchronous sequence you use to observe whether a person permitted you to update Live Activities with frequent ActivityKit push notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/frequentpushenablementupdates-swift.struct)*