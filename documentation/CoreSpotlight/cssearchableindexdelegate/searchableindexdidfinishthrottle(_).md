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

If the system previously throttled the indexing process for your app, it calls this method when throttling ends. For example, it might call this method after someone plugs in their device to charge it. Use this method to resume your app’s standard indexing behavior.

## Parameters

- `searchableIndex`: The index that was throttled.

## See Also

- [func searchableIndexDidThrottle(CSSearchableIndex)](cssearchableindexdelegate/searchableindexdidthrottle(_:).md)
  Tells the delegate that indexing is being throttled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableindexdelegate/searchableindexdidfinishthrottle(_:))*