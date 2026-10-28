# imagesWithObjectAnnotations()

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table where each row represents an image, and its columns are the image file URLs and its annotations.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

> **Deprecated**: Use gatherAnnotatedFileNames()

## Declaration

```swift
func imagesWithObjectAnnotations() throws -> MLDataTable
```

## Return Value

An [`MLDataTable`](../../mldatatable.md) containing the contents of the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/imageswithobjectannotations())*