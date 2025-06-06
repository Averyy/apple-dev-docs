# NWBrowser.Result.Change.changed(old:new:flags:)

**Framework**: Network  
**Kind**: case

A result changed properties but was not removed.

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
case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)
```

## See Also

- [NWBrowser.Result.Change.identical](nwbrowser/result/change/identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](nwbrowser/result/change/added(_:).md)
  A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](nwbrowser/result/change/removed(_:).md)
  A previously discovered result was removed.
- [NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags.md)
  Flags providing details about a change in a discovered service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change/changed(old:new:flags:))*