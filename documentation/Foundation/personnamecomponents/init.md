# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a person name components object from a given string.

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
init(_ value: String) throws
```

#### Discussion

This initializer uses a combination of locale rules and heuristics to determine the most likely name components for a particular string representation. Parsing name components from a representation created for an existing name components object may not produce equivalent results.

> ❗ **Important**:  Only names using Latin or CJK scripts are supported.

Here are some general rules that describe the name component parsing behavior:

- Names in Latin script have components delimited by whitespace.
- The format style parses names with a single delimited component into their most likely name component.
- Names in Latin script with more than two delimited components may include middle components in the `givenName`, `middleName`, or `familyName` name components.
- The format style may parse names in inverted Latin script into components in a different order than they appear. Inverted names in CJK script won’t typically produce the correct results.
- Names in Latin script may use a comma to indicate name inversion.
- Names in Latin script have capitalization preserved between string representation and parsed components.
- The format style ignores text between parentheses or brackets, as well as extraneous characters in names.

| String | Name prefix | Given name | Middle name | Family name | Name suffix |
| --- | --- | --- | --- | --- | --- |
| Thomas Clark |  | Thomas |  | Clark |  |
| Thomas Louis Clark |  | Thomas | Louis | Clark |  |
| Tom Louis Appleseed |  | Tom Louis |  | Clark |  |
| Thomas L. Appleseed |  | Thomas | L. | Clark |  |
| Dr. Thomas, Esq. | Dr. | Thomas |  |  | Esq. |
| thomas clark |  | thomas |  | clark |  |
| Clark, Thomas |  | Thomas |  | Clark |  |
| Clark Thomas |  | Thomas |  | Clark |  |
| CLARK Thomas |  | Thomas |  | CLARK |  |
| Thomas (a.k.a. Tom) Clark 🍎 |  | Thomas |  | Clark |  |
| 杨振宁 |  | 振宁 |  | 杨 |  |
| Jean-Philippe de Zélicourt |  | Jean-Philippe |  | de Zélicourt |  |
| Max Mustermann |  | Max |  | Mustermann |  |
| 木田泰夫 |  | 泰夫 |  | 木田 |  |
| José Ramiro Martín González de Rivera |  | José | Ramiro | Martín González de Rivera |  |

## Parameters

- `value`: A string to parse into name components.

## See Also

- [init<S>(S.ParseInput, strategy: S) throws](personnamecomponents/init(_:strategy:).md)
  Creates a person name components object from a given string by applying the provided parsing strategy.
- [var parseStrategy: PersonNameComponents.ParseStrategy](personnamecomponents/formatstyle/parsestrategy.md)
  The strategy used to parse a string into person name components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/personnamecomponents/init(_:))*