# RecordLabels

**Framework**: Apple Music API  
**Kind**: dictionary  
**Role**: Object

A resource object that represents a record label.

**Availability**:
- Apple Music 1.0+

## Declaration

```
object RecordLabels
```

## Topics

### Related Objects
- [object RecordLabels.Attributes](./recordlabels/attributes-data.dictionary.md)
  The attributes for a record label resource.
- [object RecordLabels.Views](./recordlabels/views-data.dictionary.md)
  The relationship views for a record label resource.

## Properties

- `id` (string) *(required)*: The identifier for the record label.
- `type` (string) *(required)*: This value must always be `record-labels`.

  **Allowed Values**: `record-labels`
- `href` (string) *(required)*: A relative location for the record label resource.
- `attributes` (RecordLabels.Attributes): The attributes of the record label.
- `views` (RecordLabels.Views): The relationship views for the record label.

## See Also

### Handling the Response
- [object RecordLabelsResponse](./recordlabelsresponse.md)
  The response to a request for record labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicapi/recordlabels)*