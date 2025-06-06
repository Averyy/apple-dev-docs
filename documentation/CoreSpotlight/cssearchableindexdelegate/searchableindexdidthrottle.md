# searchableIndexDidThrottle(_:)

**Framework**: Core Spotlight  
**Kind**: method

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

#### Discussion

In some situations, such as when the device is using battery only, the system may throttle indexing to save power. You can implement this method to be notified of this situation so that you can respond by, for example, prioritizing the items to index.

## Parameters

- `searchableIndex`: The indexing that’s being throttled.

## See Also

- [func searchableIndexDidFinishThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidfinishthrottle(_:).md)
  Tells the delegate that the index throttling has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindexdidthrottle(_:))*