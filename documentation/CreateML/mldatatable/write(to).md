# write(to:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Exports a binary file of the data table to the given directory URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func write(to directoryURL: URL) throws
```

## Parameters

- `directoryURL`: The directory location in the file system to which the data table file should be written.

## See Also

### Saving a data table
- [func write(toDirectory: String) throws](./write%28todirectory%29.md)
  Exports a binary file of the data table to the given directory path.
- [func writeCSV(to: URL) throws](./writecsv%28to%29.md)
  Exports a CSV file of the data table to the given directory URL.
- [func writeCSV(toFile: String) throws](./writecsv%28tofile%29.md)
  Exports a CSV file of the data table to the given directory path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/write(to:))*