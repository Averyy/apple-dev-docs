# MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)

**Framework**: Create ML  
**Kind**: case

An activity classifier data source that uses a directory that contains sensor data files and one annotation file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case directoryWithDataAndAnnotation(at: URL, annotationFileName: String, timeStampColumn: String, labelStartTimeColumn: String, labelEndTimeColumn: String)
```

#### Discussion

Create a data source by gathering all activity data files, and one annotation file, into a directory. Pass that directory’s [`URL`](https://developer.apple.com/documentation/Foundation/URL) and the relevant column names of the annotation file to [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](mlactivityclassifier/datasource/directorywithdataandannotation(at:annotationfilename:timestampcolumn:labelstarttimecolumn:labelendtimecolumn:).md).

## Parameters

- `at`: The location URL of a directory in the file system that contains sensor data files and an activity   annotation file.
- `annotationFileName`: The name of the activity annotation file.
- `timeStampColumn`: The name of the column that contains the timestamps for each sensor data sample.
- `labelStartTimeColumn`: The name of the column that contains the activity’s starting-time index in the   data file.
- `labelEndTimeColumn`: The name of the column that contains the activity’s ending-time index in the data   file.

## See Also

- [MLActivityClassifier.DataSource.labeledDirectories(at:)](mlactivityclassifier/datasource/labeleddirectories(at:).md)
  An activity classifier data source that uses a directory of directories that contain sensor data files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/directorywithdataandannotation(at:annotationfilename:timestampcolumn:labelstarttimecolumn:labelendtimecolumn:))*