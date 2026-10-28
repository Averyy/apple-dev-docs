# MLActivityClassifier.DataSource.labeledDirectories(at:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An activity classifier data source that uses a directory of directories that contain sensor data files.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case labeledDirectories(at: URL)
```

## Discussion

Create a data source by organizing each activity’s data files into a directory and naming each directory with the label for that activity.

> **Note**: Each data file must contain exactly one entire recording of an activity.

For example, to organize data files for an activity classifier that recognizes walking, jogging, and running, start by creating directories named “walk”, “jog”, and “run”. Place all the files of walking sensor data into the “walk” directory, and so on.

Next, gather all the activity directories into a directory and pass its [`URL`](../../../Foundation/url.md) to [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](./labeleddirectories%28at%29.md).

## Parameters

- `at`: A [`URL`](../../../Foundation/url.md) of a directory in the file system that contains directories, each named with an activity label for the sensor data files.

## See Also

### Creating a data source
- [case directoryWithDataAndAnnotation(at: URL, annotationFileName: String, timeStampColumn: String, labelStartTimeColumn: String, labelEndTimeColumn: String)](./directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md)
  An activity classifier data source that uses a directory that contains sensor data files and one annotation file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/labeleddirectories(at:))*