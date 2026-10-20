# NWBrowser.Result.Change.Flags

**Framework**: Network  
**Kind**: struct  
**Role**: Structure

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
- [static let identical: NWBrowser.Result.Change.Flags](./flags/identical.md)
  The results are identical.
- [static let interfaceAdded: NWBrowser.Result.Change.Flags](./flags/interfaceadded.md)
  The service was discovered over a new interface.
- [static let interfaceRemoved: NWBrowser.Result.Change.Flags](./flags/interfaceremoved.md)
  The service was no longer discovered over a certain interface.
- [static let metadataChanged: NWBrowser.Result.Change.Flags](./flags/metadatachanged.md)
  The service’s associated metadata changed.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../../../Swift/hashable.md)
- [OptionSet](../../../../Swift/optionset.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)
- [SetAlgebra](../../../../Swift/setalgebra.md)

## See Also

### Inspecting Change Types
- [NWBrowser.Result.Change.identical](./identical.md)
  No change was detected for the result.
- [NWBrowser.Result.Change.added(_:)](./added%28_%29.md)
  A new result was discovered.
- [NWBrowser.Result.Change.removed(_:)](./removed%28_%29.md)
  A previously discovered result was removed.
- [case changed(old: NWBrowser.Result, new: NWBrowser.Result, flags: NWBrowser.Result.Change.Flags)](./changed%28old,new,flags%29.md)
  A result changed properties but was not removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwbrowser/result/change/flags)*