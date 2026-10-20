# containsHeader

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether an input CSV file contains a header.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var containsHeader: Bool
```

#### Discussion

Set `containsHeader` to `false` when the first row in a CSV contains usable data. Because every column in a data table needs a name, `MLDataTable` names the columns `X1`, `X2`, … `X`*n* in the same order as they appear in the CSV file.

## See Also

### Specifying the CSV file format
- [var delimiter: String](./delimiter.md)
  The character that separates the data fields in a CSV file.
- [var lineTerminator: String](./lineterminator.md)
  The character that represents the end of a line in a CSV file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/parsingoptions/containsheader)*