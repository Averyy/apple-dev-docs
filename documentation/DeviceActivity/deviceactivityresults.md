# DeviceActivityResults

**Framework**: DeviceActivity  
**Kind**: struct

An asynchronous sequence of filtered device activity results.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct DeviceActivityResults<Element>
```

## Topics

### Classes
- [DeviceActivityResults.Iterator](deviceactivityresults/iterator.md)
  An asynchronous iterator for filtered device activity.
### Instance Methods
- [func makeAsyncIterator() -> DeviceActivityResults<Element>.Iterator<Element>](deviceactivityresults/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
### Type Aliases
- [DeviceActivityResults.AsyncIterator](deviceactivityresults/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](deviceactivityresults/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityresults)*