# searchableIndexDidFinishThrottle(_:)

**Framework**: Core Spotlight  
**Kind**: method

Tells the delegate that the index throttling has finished.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
optional func searchableIndexDidFinishThrottle(_ searchableIndex: CSSearchableIndex)
```

#### Discussion

In some situations, such as when the device is using battery only, the system may throttle indexing to save power. You can implement this method to be notified when throttling is finished so that your app can resume its standard indexing behavior.

## Parameters

- `searchableIndex`: The index that was throttled.

## See Also

- [func searchableIndexDidThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidthrottle(_:).md)
  Tells the delegate that indexing is being throttled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindexdidfinishthrottle(_:))*