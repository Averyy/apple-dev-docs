# Data visualizations

**Framework**: Create ML  
**Role**: API Collection

Render images of data tables and columns in a playground.

## Topics

### Table visualizations
- [func show(MLDataTable) -> any MLStreamingVisualizable](./show%28_%29-2dkfz.md)
  Generates a streaming visualization of the data table.
### Column visualizations
- [func show<Element>(MLDataColumn<Element>) -> any MLStreamingVisualizable](./show%28_%29-5r938.md)
  Generates a streaming visualization of the data column.
- [func show(MLUntypedColumn) -> any MLStreamingVisualizable](./show%28_%29-9645r.md)
  Generates a streaming visualization of the untyped column.
### Plot visualizations
- [func show<ElementX, ElementY>(MLDataColumn<ElementX>, MLDataColumn<ElementY>) -> any MLStreamingVisualizable](./show%28_,_%29-537qb.md)
  Generates a streaming plot visualization of the two data columns.
- [func show(MLUntypedColumn, MLUntypedColumn) -> any MLStreamingVisualizable](./show%28_,_%29-2tmbf.md)
  Generates a streaming plot visualization of the two untyped columns.
### Visualization protocols
- [protocol MLVisualizable](./mlvisualizable.md)
  An image visualization of machine learning types.
- [protocol MLStreamingVisualizable](./mlstreamingvisualizable.md)
  A sequence of image visualizations for machine learning types.

## See Also

### Tabular data
- [struct MLDataTable](./mldatatable.md)
  A table of data for training or evaluating a machine learning model.
- [enum MLDataValue](./mldatavalue.md)
  The value of a cell in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/data-visualizations)*