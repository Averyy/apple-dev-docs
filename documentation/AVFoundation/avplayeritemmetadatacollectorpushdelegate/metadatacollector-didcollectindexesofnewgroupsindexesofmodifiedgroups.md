# metadataCollector(_:didCollect:indexesOfNewGroups:indexesOfModifiedGroups:)

**Framework**: AVFoundation  
**Kind**: method  
**Required**: Yes

Tells the delegate the collected metadata group information has changed and needs to be updated.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
func metadataCollector(_ metadataCollector: AVPlayerItemMetadataCollector, didCollect metadataGroups: sending [AVDateRangeMetadataGroup], indexesOfNewGroups: IndexSet, indexesOfModifiedGroups: IndexSet)
```

#### Discussion

This method is called when additions or modifications are made to the array of collected metadata groups. The initial invocation will have `indexesOfNewGroup` referring to every index in `metadataGroups`. Subsequent invocations may not contain all previously collected metadata groups if they no longer refer to a region in the player item’s [`seekableTimeRanges`](avplayeritem/seekabletimeranges.md).

## Parameters

- `metadataCollector`: The   on which this delegate is set.
- `metadataGroups`: The complete array of all metadata groups meeting the criteria of the output.
- `indexesOfNewGroups`: The indexes of the   added since the last delegate invocation of this method.
- `indexesOfModifiedGroups`: The indexes of the   modified since the last delegate invocation of this method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemmetadatacollectorpushdelegate/metadatacollector(_:didcollect:indexesofnewgroups:indexesofmodifiedgroups:))*