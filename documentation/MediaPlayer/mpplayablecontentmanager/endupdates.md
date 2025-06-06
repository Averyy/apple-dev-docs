# endUpdates()

**Framework**: Media Player  
**Kind**: method

Ends a synchronized update.

**Availability**:
- iOS 7.1+
- iPadOS 7.1+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func endUpdates()
```

#### Discussion

Call this method upon completion of the batch updates. If you call this method in the middle of an update, all updates stop and you’ll need to apply remaining updates at a later time.

## See Also

- [func beginUpdates()](mpplayablecontentmanager/beginupdates.md)
  Updates several Media Player content items at once.
- [func reloadData()](mpplayablecontentmanager/reloaddata.md)
  Reloads the data from the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpplayablecontentmanager/endupdates())*