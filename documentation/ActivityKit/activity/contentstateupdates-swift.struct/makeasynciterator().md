# makeAsyncIterator()

**Framework**: ActivityKit  
**Kind**: method  
**Role**: Instance Method

Creates the asynchronous iterator that produces results from this asynchronous sequence.

**Availability**:
- iOS 16.1+ - Deprecated in 16.2
- iPadOS 16.1+ - Deprecated in 16.2

> **Deprecated**: Use `ContentUpdates` instead

## Declaration

```swift
func makeAsyncIterator() -> Activity<Attributes>.ContentStateUpdates.Iterator
```

## See Also

### Creating an iterator
- [Activity.ContentStateUpdates.Iterator](./iterator.md)
  An iterator for accessing individual data entries from the series.
- [Activity.ContentStateUpdates.Element](./element.md)
  The type of element this asynchronous sequence produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentstateupdates-swift.struct/makeasynciterator())*