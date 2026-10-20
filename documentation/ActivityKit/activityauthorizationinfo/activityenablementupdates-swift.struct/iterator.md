# ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator

**Framework**: ActivityKit  
**Kind**: struct  
**Role**: Structure

An iterator for accessing individual data entries from the series.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> Bool?](./iterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> ActivityAuthorizationInfo.ActivityEnablementUpdates.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
- [ActivityAuthorizationInfo.ActivityEnablementUpdates.Element](./element.md)
  The type of element this asynchronous sequence produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.struct/iterator)*