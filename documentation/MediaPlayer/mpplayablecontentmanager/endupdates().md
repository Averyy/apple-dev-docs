# endUpdates()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Ends a synchronized update.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
func endUpdates()
```

```objc
- (void) endUpdates;
```

## Discussion

Call this method upon completion of the batch updates. If you call this method in the middle of an update, all updates stop and you’ll need to apply remaining updates at a later time.

## See Also

### Updating data
- [func beginUpdates()](./beginupdates%28%29.md)
  Updates several Media Player content items at once.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/endupdates())*