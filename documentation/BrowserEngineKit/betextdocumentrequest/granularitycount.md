# granularityCount

**Framework**: BrowserEngineKit  
**Kind**: property

A count of granularity units that defines the scope of the document request.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var granularityCount: Int { get set }
```

#### Discussion

Use this value with [`surroundingGranularity`](betextdocumentrequest/surroundinggranularity.md) to determine the extent of the text context that the system requests.

## See Also

- [var surroundingGranularity: UITextGranularity](betextdocumentrequest/surroundinggranularity.md)
  The unit of measurement for the document request’s scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentrequest/granularitycount)*