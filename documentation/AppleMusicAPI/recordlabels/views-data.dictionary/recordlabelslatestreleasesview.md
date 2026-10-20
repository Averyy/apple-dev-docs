# RecordLabels.Views.RecordLabelsLatestReleasesView

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A relationship view from this record label to a selection of its latest releases.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object RecordLabels.Views.RecordLabelsLatestReleasesView
```

## Topics

### Related Objects
- [object RecordLabels.Views.RecordLabelsLatestReleasesView.Attributes](./recordlabelslatestreleasesview/attributes-data.dictionary.md)
  The attributes for the record label latest releases view.

## Properties

- `href` (string): A relative location for the view.
- `next` (string): A relative cursor to fetch the next paginated collection of resources in the view if more exist.
- `attributes` (RecordLabels.Views.RecordLabelsLatestReleasesView.Attributes) *(required)*: The attributes for the view.
- `data` ([Albums]) *(required)*: A selection of latest releases from this record label.

## See Also

### Related Objects
- [object RecordLabels.Views.RecordLabelsTopReleasesView](./recordlabelstopreleasesview.md)
  A relationship view from this record label to a selection of its top releases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/recordlabels/views-data.dictionary/recordlabelslatestreleasesview)*