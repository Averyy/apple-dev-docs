# write(toDirectory:)

**Framework**: Create ML  
**Kind**: method

Exports a binary file of the data table to the given directory path.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func write(toDirectory path: String) throws
```

## Parameters

- `path`: A file system directory path where the data table file should be written.

## See Also

- [func write(to: URL) throws](mldatatable/write(to:).md)
  Exports a binary file of the data table to the given directory URL.
- [func writeCSV(to: URL) throws](mldatatable/writecsv(to:).md)
  Exports a CSV file of the data table to the given directory URL.
- [func writeCSV(toFile: String) throws](mldatatable/writecsv(tofile:).md)
  Exports a CSV file of the data table to the given directory path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/write(todirectory:))*