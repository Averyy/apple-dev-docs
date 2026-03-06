# init(hasHeaderRow:nilEncodings:trueEncodings:falseEncodings:floatingPointType:ignoresEmptyLines:usesQuoting:usesEscaping:delimiter:escapeCharacter:)

**Framework**: TabularData  
**Kind**: init

Creates a set of options for reading a CSV file.

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
init(hasHeaderRow: Bool = true, nilEncodings: Set<String> = ["", "#N/A", "#N/A N/A", "#NA", "N/A", "NA", "NULL", "n/a", "nil", "null"], trueEncodings: Set<String> = ["1", "True", "TRUE", "true"], falseEncodings: Set<String> = ["0", "False", "FALSE", "false"], floatingPointType: CSVType = .double, ignoresEmptyLines: Bool = true, usesQuoting: Bool = true, usesEscaping: Bool = false, delimiter: Character = Character(","), escapeCharacter: Character = Character("\\"))
```

## Parameters

- `hasHeaderRow`: A Boolean value that indicates whether the CSV file has a header row. Defaults to `true`.
- `nilEncodings`: A list of recognized encodings of `nil`. Defaults to `["", "#N/A", "#N/A N/A", "#NA", "N/A", "NA", "NULL", "n/a", "null"]`.
- `trueEncodings`: A list of acceptable encodings of `true`. Defaults to `["1", "True", "TRUE", "true"]`.
- `falseEncodings`: A list of acceptable encodings of `false`. Defaults to `["0", "False", "FALSE", "false"]`.
- `floatingPointType`: A type to use for floating-point numeric values (either [`CSVType.double`](csvtype/double.md) or [`CSVType.float`](csvtype/float.md)). Defaults to [`CSVType.double`](csvtype/double.md).
- `ignoresEmptyLines`: A Boolean value that indicates whether to ignore empty lines. Defaults to `true.`
- `usesQuoting`: A Boolean value that indicates whether the CSV file uses quoting. Defaults to `true`.
- `usesEscaping`: A Boolean value that indicates whether the CSV file uses escaping sequences. Defaults to `false`.
- `delimiter`: A field delimiter. Defaults to comma (`,`).
- `escapeCharacter`: An escape character to use if [`usesEscaping`](csvreadingoptions/usesescaping.md) is true. Defaults to backslash (`\`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/init(hasheaderrow:nilencodings:trueencodings:falseencodings:floatingpointtype:ignoresemptylines:usesquoting:usesescaping:delimiter:escapecharacter:))*