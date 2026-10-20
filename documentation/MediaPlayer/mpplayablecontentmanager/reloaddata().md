# reloadData()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Reloads the data from the data source.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
func reloadData()
```

```objc
- (void) reloadData;
```

#### Discussion

Call this method when the data source changed, which notifies the content manager to reload the data from the data source.

## See Also

### Updating data
- [func beginUpdates()](./beginupdates%28%29.md)
  Updates several Media Player content items at once.
- [func endUpdates()](./endupdates%28%29.md)
  Ends a synchronized update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/reloaddata())*