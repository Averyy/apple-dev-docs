# NWBrowser.Result.Change.added(_:)

**Framework**: Network  
**Kind**: case  
**Role**: Case

A new result was discovered.

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
case added(NWBrowser.Result)
```

## See Also

### Inspecting Change Types
- [NWBrowser.Result.Change.identical](./identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.removed(_:)](./removed%28_%29.md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](./changed%28old,new,flags%29.md)
  A result changed properties but was not removed.
- [NWBrowser.Result.Change.Flags](./flags.md)
  Flags providing details about a change in a discovered service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change/added(_:))*