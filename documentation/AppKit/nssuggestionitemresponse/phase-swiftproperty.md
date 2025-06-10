# phase

**Framework**: AppKit  
**Kind**: property

Describes the phase of results. In other words, whether this batch of items represents an intermediate set of results–and more are coming, or whether these results are complete/final. Defaults to `.final`.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var phase: NSSuggestionItemResponse<SuggestionItemType>.Phase
```

#### Discussion

> **Note**: This controls whether or not a indeterminate spinner appears by the control and suggestions menu to indicate to the user that there may be any/more/different/updated suggestions coming.

> **Note**: Once a final set of results have been provided, the control will ignore subsequent provisions until the search request changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssuggestionitemresponse/phase-swift.property)*