# Activity.ContentUpdates

**Framework**: ActivityKit  
**Kind**: struct

A structure that offers functionality to observe changes to the dynamic content of a Live Activity.

**Availability**:
- iOS 16.2+
- iPadOS 16.2+

## Declaration

```swift
struct ContentUpdates
```

## Topics

### Structures
- [Activity.ContentUpdates.Iterator](activity/contentupdates-swift.struct/iterator.md)
  An iterator for accessing individual data entries from the series.
### Instance Methods
- [func makeAsyncIterator() -> Activity<Attributes>.ContentUpdates.Iterator](activity/contentupdates-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces results from this asynchronous sequence.
### Type Aliases
- [Activity.ContentUpdates.AsyncIterator](activity/contentupdates-swift.struct/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
- [Activity.ContentUpdates.Element](activity/contentupdates-swift.struct/element.md)
  The type of element this asynchronous sequence produces.
### Default Implementations
- [AsyncSequence Implementations](activity/contentupdates-swift.struct/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [var contentUpdates: Activity<Attributes>.ContentUpdates](activity/contentupdates-swift.property.md)
  An asynchronous sequence you use to observe changes to the dynamic content of a Live Activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activity/contentupdates-swift.struct)*