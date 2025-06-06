# NSSelectionGranularity

**Framework**: AppKit  
**Kind**: enum

These constants specify how much the text view extends the selection when the user drags the mouse. They’re used by [`selectionGranularity`](nstextview/selectiongranularity.md), and [`selectionRange(forProposedRange:granularity:)`](nstextview/selectionrange(forproposedrange:granularity:).md):

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSSelectionGranularity
```

## Topics

### Constants
- [NSSelectionGranularity.selectByCharacter](nsselectiongranularity/selectbycharacter.md)
  Extends the selection character by character.
- [NSSelectionGranularity.selectByWord](nsselectiongranularity/selectbyword.md)
  Extends the selection word by word.
- [NSSelectionGranularity.selectByParagraph](nsselectiongranularity/selectbyparagraph.md)
  Extends the selection paragraph by paragraph.
### Initializers
- [init?(rawValue: UInt)](nsselectiongranularity/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum NSSelectionAffinity](nsselectionaffinity.md)
  These constants specify the preferred direction of selection. They’re used by [`selectionAffinity`](nstextview/selectionaffinity.md) and [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md).
- [enum NSFindPanelAction](nsfindpanelaction.md)
  These constants define the tags for [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md).
- [Input Sources Locale Identifiers](input-sources-locale-identifiers.md)
  Locale identifiers represent the input sources available.
- [Find Panel Search Metadata](find-panel-search-metadata.md)
  In addition to communicating search strings via the find pasteboard, the standard Find panel for `NSTextView` also communicates search option metadata, including case sensitivity and substring matching options. This metadata is stored in a property list as the [`findPanelSearchOptions`](nspasteboard/pasteboardtype/findpanelsearchoptions.md) value on the global find pasteboard. As such, third party applications may store additional keys in this property list to communicate additional metadata as desired to support the various search options common to many third-party applications’ Find panels.
- [enum NSFindPanelSubstringMatchType](nsfindpanelsubstringmatchtype.md)
  The type of substring matching used by the Find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsselectiongranularity)*