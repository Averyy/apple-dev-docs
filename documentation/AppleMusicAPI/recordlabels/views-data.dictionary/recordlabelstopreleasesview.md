# RecordLabels.Views.RecordLabelsTopReleasesView

**Framework**: Apple Music API  
**Kind**: dictionary

A relationship view from this record label to a selection of its top releases.

**Availability**:
- Apple Music 1.0+

## Declaration

```swift
object RecordLabels.Views.RecordLabelsTopReleasesView
```

## Topics

### Related Objects
- [object RecordLabels.Views.RecordLabelsTopReleasesView.Attributes](recordlabels/views-data.dictionary/recordlabelstopreleasesview/attributes-data.dictionary.md)
  The attributes for the record label top releases view.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (RecordLabels.Views.RecordLabelsTopReleasesView.Attributes) *(required)*: The attributes for the view.
- `data` ([Albums]) *(required)*: A selection of top releases from this record label.

## See Also

- [object RecordLabels.Views.RecordLabelsLatestReleasesView](recordlabels/views-data.dictionary/recordlabelslatestreleasesview.md)
  A relationship view from this record label to a selection of its latest releases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/recordlabels/views-data.dictionary/recordlabelstopreleasesview)*