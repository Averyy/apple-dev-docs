# granularityCount

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) NSInteger granularityCount;
```

#### Discussion

Use this value with [`surroundingGranularity`](./surroundinggranularity.md) to determine the extent of the text context that the system requests.

## See Also

### Scoping the document request
- [var surroundingGranularity: UITextGranularity](./surroundinggranularity.md)
  The unit of measurement for the document request’s scope.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentrequest/granularitycount)*