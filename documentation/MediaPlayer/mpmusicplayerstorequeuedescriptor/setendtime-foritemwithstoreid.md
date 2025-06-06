# setEndTime(_:forItemWithStoreID:)

**Framework**: Media Player  
**Kind**: method

Sets the time the designated store item is to stop playing.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setEndTime(_ endTime: TimeInterval, forItemWithStoreID storeID: String)
```

## Parameters

- `endTime`: The   describing when the store item stops playing.
- `storeID`: The store identifier associated with the item in the queue that has a changed end time.

## See Also

- [func setStartTime(TimeInterval, forItemWithStoreID: String)](mpmusicplayerstorequeuedescriptor/setstarttime(_:foritemwithstoreid:).md)
  Sets the time the designated store item is to start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/setendtime(_:foritemwithstoreid:))*