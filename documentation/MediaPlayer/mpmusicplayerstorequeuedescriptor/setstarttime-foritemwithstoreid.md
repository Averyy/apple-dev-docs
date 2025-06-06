# setStartTime(_:forItemWithStoreID:)

**Framework**: Media Player  
**Kind**: method

Sets the time the designated store item is to start playing.

**Availability**:
- iOS 10.1+
- iPadOS 10.1+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func setStartTime(_ startTime: TimeInterval, forItemWithStoreID storeID: String)
```

## Parameters

- `startTime`: The   describing when the store item starts playing.
- `storeID`: The store identifier associated with the item in the queue that has a changed start time.

## See Also

- [func setEndTime(TimeInterval, forItemWithStoreID: String)](mpmusicplayerstorequeuedescriptor/setendtime(_:foritemwithstoreid:).md)
  Sets the time the designated store item is to stop playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/setstarttime(_:foritemwithstoreid:))*