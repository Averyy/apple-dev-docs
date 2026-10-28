# beginUpdates()

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Updates several Media Player content items at once.

**Availability**:
- iOS 7.1+ - Deprecated in 14.0
- iPadOS 7.1+ - Deprecated in 14.0
- Mac Catalyst 13.1+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use CarPlay framework

## Declaration

```swift
func beginUpdates()
```

```objc
- (void) beginUpdates;
```

## Discussion

Call this method to start a synchronized batch update of `MPContentItems` objects.

## See Also

### Updating data
- [func endUpdates()](./endupdates%28%29.md)
  Ends a synchronized update.
- [func reloadData()](./reloaddata%28%29.md)
  Reloads the data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/beginupdates())*