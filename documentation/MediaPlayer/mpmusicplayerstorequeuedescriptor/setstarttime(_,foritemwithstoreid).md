# setStartTime(_:forItemWithStoreID:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setStartTime:(NSTimeInterval) startTime forItemWithStoreID:(NSString *) storeID;
```

## Parameters

- `startTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the store item starts playing.
- `storeID`: The store identifier associated with the item in the queue that has a changed start time.

## See Also

### Setting start and end times
- [func setEndTime(TimeInterval, forItemWithStoreID: String)](./setendtime%28_,foritemwithstoreid%29.md)
  Sets the time the designated store item is to stop playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/setstarttime(_:foritemwithstoreid:))*