# init(includesHeader:nilEncoding:trueEncoding:falseEncoding:newline:delimiter:)

**Framework**: TabularData  
**Kind**: init

Creates a set of options for writing a CSV file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
init(includesHeader: Bool = true, nilEncoding: String = "", trueEncoding: String = "true", falseEncoding: String = "false", newline: String = "\n", delimiter: Character = ",")
```

## Parameters

- `includesHeader`: A Boolean value that indicates whether to write a header with the column names. Defaults to   .
- `nilEncoding`: The spelling for nil values. Defaults to an empty string.
- `trueEncoding`: The spelling for true Boolean values. Defaults to  .
- `falseEncoding`: The spelling for false Boolean values. Defaults to  .
- `newline`: The newline sequence. Defaults to a line feed.
- `delimiter`: The field delimiter. Defaults to comma ( ).


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvwritingoptions/init(includesheader:nilencoding:trueencoding:falseencoding:newline:delimiter:))*