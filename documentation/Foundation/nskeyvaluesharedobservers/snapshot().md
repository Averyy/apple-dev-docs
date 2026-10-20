# snapshot()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

A momentary snapshot of all observers added to the collection thus far, that can be assigned to an observable using `-[NSObject setSharedObservers:]`

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func snapshot() -> NSKeyValueSharedObserversSnapshot
```

```objc
- (NSKeyValueSharedObserversSnapshot *) snapshot;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyvaluesharedobservers/snapshot())*