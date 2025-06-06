# NWBrowser.Result.Change.added(_:)

**Framework**: Network  
**Kind**: case

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

- [NWBrowser.Result.Change.identical](nwbrowser/result/change/identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.removed(_:)](nwbrowser/result/change/removed(_:).md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](nwbrowser/result/change/changed(old:new:flags:).md)
  A result changed properties but was not removed.
- [NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags.md)
  Flags providing details about a change in a discovered service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change/added(_:))*