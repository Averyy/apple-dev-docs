# setEndTime(_:forItemWithStoreID:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setEndTime:(NSTimeInterval) endTime forItemWithStoreID:(NSString *) storeID;
```

## Parameters

- `endTime`: The [`TimeInterval`](../../Foundation/timeinterval.md) describing when the store item stops playing.
- `storeID`: The store identifier associated with the item in the queue that has a changed end time.

## See Also

### Setting start and end times
- [func setStartTime(TimeInterval, forItemWithStoreID: String)](./setstarttime%28_,foritemwithstoreid%29.md)
  Sets the time the designated store item is to start playing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmusicplayerstorequeuedescriptor/setendtime(_:foritemwithstoreid:))*