# NWBrowser.Result.Change

**Framework**: Network  
**Kind**: enum  
**Role**: Enumeration

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
- [NWBrowser.Result.Change.identical](./change/identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](./change/added%28_%29.md)
  A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](./change/removed%28_%29.md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](./change/changed%28old,new,flags%29.md)
  A result changed properties but was not removed.
- [NWBrowser.Result.Change.Flags](./change/flags.md)
  Flags providing details about a change in a discovered service.
### Calculating Result Changes
- [init(between: NWBrowser.Result?, NWBrowser.Result?)](./change/init%28between,_%29.md)
  Initializes a change between two results.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change)*