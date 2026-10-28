# searchableIndexDidThrottle(_:)

**Framework**: Core Spotlight  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that indexing is being throttled.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func searchableIndexDidThrottle(_ searchableIndex: CSSearchableIndex)
```

```objc
- (void) searchableIndexDidThrottle:(CSSearchableIndex *) searchableIndex;
```

## Discussion

To save power, the system can reduce the amount of time it spends indexing your app’s items. For example, the system might throttle indexing if the device is running on battery only. The system calls this method to let you know when throttling occurs, so you can prioritize the items you want to index.

## Parameters

- `searchableIndex`: The indexing that’s being throttled.

## See Also

### Monitoring Spotlight status
- [func searchableIndexDidFinishThrottle(CSSearchableIndex)](./searchableindexdidfinishthrottle%28_%29.md)
  Tells the delegate that the index throttling has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindexdidthrottle(_:))*