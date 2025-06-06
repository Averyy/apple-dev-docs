# NWBrowser.Result.Change.Flags

**Framework**: Network  
**Kind**: struct

Flags providing details about a change in a discovered service.

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
struct Flags
```

## Topics

### Change Flags
- [static let identical: NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags/identical.md)
  The results are identical.
- [static let interfaceAdded: NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags/interfaceadded.md)
  The service was discovered over a new interface.
- [static let interfaceRemoved: NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags/interfaceremoved.md)
  The service was no longer discovered over a certain interface.
- [static let metadataChanged: NWBrowser.Result.Change.Flags](nwbrowser/result/change/flags/metadatachanged.md)
  The service’s associated metadata changed.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [NWBrowser.Result.Change.identical](nwbrowser/result/change/identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](nwbrowser/result/change/added(_:).md)
  A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](nwbrowser/result/change/removed(_:).md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](nwbrowser/result/change/changed(old:new:flags:).md)
  A result changed properties but was not removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change/flags)*