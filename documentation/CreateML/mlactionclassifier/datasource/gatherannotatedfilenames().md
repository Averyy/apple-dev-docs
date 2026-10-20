# gatherAnnotatedFileNames()

**Framework**: Create ML  
**Kind**: method

Processes the data source and returns a data frame that contains file URLs and annotations.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func gatherAnnotatedFileNames() throws -> DataFrame?
```

#### Discussion

This method collects file names from the filesystem if necessary. If the data source is already in table format it renames the columns to the default column names. This method returns nil if the data source contains key points.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/gatherannotatedfilenames())*