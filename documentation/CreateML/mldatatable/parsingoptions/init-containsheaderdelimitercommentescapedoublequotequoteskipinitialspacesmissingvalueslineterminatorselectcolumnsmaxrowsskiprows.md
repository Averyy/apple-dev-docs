# init(containsHeader:delimiter:comment:escape:doubleQuote:quote:skipInitialSpaces:missingValues:lineTerminator:selectColumns:maxRows:skipRows:)

**Framework**: Create ML  
**Kind**: init

Creates CSV parsing options.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(containsHeader: Bool = true, delimiter: String = ",", comment: String = "", escape: String = "\\", doubleQuote: Bool = true, quote: String = "\"", skipInitialSpaces: Bool = true, missingValues: [String] = ["NA"], lineTerminator: String = "\n", selectColumns: [String]? = nil, maxRows: Int? = nil, skipRows: Int = 0)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/parsingoptions/init(containsheader:delimiter:comment:escape:doublequote:quote:skipinitialspaces:missingvalues:lineterminator:selectcolumns:maxrows:skiprows:))*