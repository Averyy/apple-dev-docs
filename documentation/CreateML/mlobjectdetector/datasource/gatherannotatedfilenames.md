# gatherAnnotatedFileNames()

**Framework**: Create ML  
**Kind**: method

Processes the data source and returns a data frame that contains file URLs and annotations.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func gatherAnnotatedFileNames() throws -> DataFrame
```

#### Discussion

This method collects file names from the filesystem if necessary. If the data source is already in table format it renames the columns to the default column names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/gatherannotatedfilenames())*