# Input Sources Locale Identifiers

**Framework**: AppKit

Locale identifiers represent the input sources available.

## Topics

### Constants
- [let NSAllRomanInputSourcesLocaleIdentifier: String](nsallromaninputsourceslocaleidentifier.md)
  A meta-locale identifier representing the set of Roman input sources available. You can pass `[NSArray arrayWithObject: NSAllRomanInputSourcesLocaleIdentifier]` to the [`allowedInputSourceLocales`](nstextview/allowedinputsourcelocales.md) property to restrict allowed input sources to Roman only.

## See Also

- [enum NSSelectionGranularity](nsselectiongranularity.md)
  These constants specify how much the text view extends the selection when the user drags the mouse. They’re used by [`selectionGranularity`](nstextview/selectiongranularity.md), and [`selectionRange(forProposedRange:granularity:)`](nstextview/selectionrange(forproposedrange:granularity:).md):
- [enum NSSelectionAffinity](nsselectionaffinity.md)
  These constants specify the preferred direction of selection. They’re used by [`selectionAffinity`](nstextview/selectionaffinity.md) and [`setSelectedRange(_:affinity:stillSelecting:)`](nstextview/setselectedrange(_:affinity:stillselecting:).md).
- [enum NSFindPanelAction](nsfindpanelaction.md)
  These constants define the tags for [`performFindPanelAction(_:)`](nstextview/performfindpanelaction(_:).md).
- [Find Panel Search Metadata](find-panel-search-metadata.md)
  In addition to communicating search strings via the find pasteboard, the standard Find panel for `NSTextView` also communicates search option metadata, including case sensitivity and substring matching options. This metadata is stored in a property list as the [`findPanelSearchOptions`](nspasteboard/pasteboardtype/findpanelsearchoptions.md) value on the global find pasteboard. As such, third party applications may store additional keys in this property list to communicate additional metadata as desired to support the various search options common to many third-party applications’ Find panels.
- [enum NSFindPanelSubstringMatchType](nsfindpanelsubstringmatchtype.md)
  The type of substring matching used by the Find panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/input-sources-locale-identifiers)*