# NSFindPanelSubstringMatchType

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The type of substring matching used by the Find panel.

**Availability**:
- macOS

## Declaration

```swift
enum NSFindPanelSubstringMatchType
```

```c
enum NSFindPanelSubstringMatchType : NSUInteger;
```

## Topics

### Constants
- [NSFindPanelSubstringMatchType.contains](./nsfindpanelsubstringmatchtype/contains.md)
- [NSFindPanelSubstringMatchType.startsWith](./nsfindpanelsubstringmatchtype/startswith.md)
- [NSFindPanelSubstringMatchType.fullWord](./nsfindpanelsubstringmatchtype/fullword.md)
- [NSFindPanelSubstringMatchType.endsWith](./nsfindpanelsubstringmatchtype/endswith.md)
### Initializers
- [init?(rawValue: UInt)](./nsfindpanelsubstringmatchtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum NSSelectionGranularity](./nsselectiongranularity.md)
  These constants specify how much the text view extends the selection when the user drags the mouse. They’re used by [`selectionGranularity`](./nstextview/selectiongranularity.md), and [`selectionRange(forProposedRange:granularity:)`](./nstextview/selectionrange%28forproposedrange,granularity%29.md):
- [enum NSSelectionAffinity](./nsselectionaffinity.md)
  These constants specify the preferred direction of selection. They’re used by [`selectionAffinity`](./nstextview/selectionaffinity.md) and [`setSelectedRange(_:affinity:stillSelecting:)`](./nstextview/setselectedrange%28_,affinity,stillselecting%29.md).
- [enum NSFindPanelAction](./nsfindpanelaction.md)
  These constants define the tags for [`performFindPanelAction(_:)`](./nstextview/performfindpanelaction%28_%29.md).
- [Input Sources Locale Identifiers](./input-sources-locale-identifiers.md)
  Locale identifiers represent the input sources available.
- [Find Panel Search Metadata](./find-panel-search-metadata.md)
  In addition to communicating search strings via the find pasteboard, the standard Find panel for `NSTextView` also communicates search option metadata, including case sensitivity and substring matching options. This metadata is stored in a property list as the [`findPanelSearchOptions`](./nspasteboard/pasteboardtype/findpanelsearchoptions.md) value on the global find pasteboard. As such, third party applications may store additional keys in this property list to communicate additional metadata as desired to support the various search options common to many third-party applications’ Find panels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfindpanelsubstringmatchtype)*