# NWBrowser.Result.Change

**Framework**: Network  
**Kind**: enum

Ways in which discovered services can change between specific results.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum Change
```

## Topics

### Inspecting Change Types
- [NWBrowser.Result.Change.identical](nwbrowser/result/change/identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](nwbrowser/result/change/added(_:).md)
  A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](nwbrowser/result/change/removed(_:).md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](nwbrowser/result/change/changed(old:new:flags:).md)
  A result changed properties but was not removed.
- [NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags.md)
  Flags providing details about a change in a discovered service.
### Calculating Result Changes
- [init(between: NWBrowser.Result?, NWBrowser.Result?)](nwbrowser/result/change/init(between:_:).md)
  Initializes a change between two results.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change)*