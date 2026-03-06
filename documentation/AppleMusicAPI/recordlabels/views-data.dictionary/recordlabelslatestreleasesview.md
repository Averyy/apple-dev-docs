# RecordLabels.Views.RecordLabelsLatestReleasesView

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship view from this record label to a selection of its latest releases.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object RecordLabels.Views.RecordLabelsLatestReleasesView
```

## Topics

### Related Objects
- [object RecordLabels.Views.RecordLabelsLatestReleasesView.Attributes](recordlabels/views-data.dictionary/recordlabelslatestreleasesview/attributes-data.dictionary.md)
  The attributes for the record label latest releases view.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (RecordLabels.Views.RecordLabelsLatestReleasesView.Attributes) *(required)*: The attributes for the view.
- `data` ([Albums]) *(required)*: A selection of latest releases from this record label.

## See Also

- [object RecordLabels.Views.RecordLabelsTopReleasesView](recordlabels/views-data.dictionary/recordlabelstopreleasesview.md)
  A relationship view from this record label to a selection of its top releases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/recordlabels/views-data.dictionary/recordlabelslatestreleasesview)*