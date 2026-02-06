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

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [struct DeviceActivityFilter](deviceactivityfilter.md)
  A type that filters the device activity data to include in a report.
- [struct DeviceActivityData](deviceactivitydata.md)
  Activity data for a person on a specific device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityresults)*