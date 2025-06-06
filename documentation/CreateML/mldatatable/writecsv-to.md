# writeCSV(to:)

**Framework**: Create ML  
**Kind**: method

Exports a CSV file of the data table to the given directory URL.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func writeCSV(to fileURL: URL) throws
```

#### Discussion

- fileURL: The location in the file system to which the data table file should be written.

## See Also

- [func write(to: URL) throws](mldatatable/write(to:).md)
  Exports a binary file of the data table to the given directory URL.
- [func write(toDirectory: String) throws](mldatatable/write(todirectory:).md)
  Exports a binary file of the data table to the given directory path.
- [func writeCSV(toFile: String) throws](mldatatable/writecsv(tofile:).md)
  Exports a CSV file of the data table to the given directory path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/writecsv(to:))*