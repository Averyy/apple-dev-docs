# request(_:didProduce:)

**Framework**: Sound Analysis  
**Kind**: method  
**Required**: Yes

Provides a new analysis result to your app with the specified time range.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func request(_ request: any SNRequest, didProduce result: any SNResult)
```

#### Discussion

The analyzer calls this function each time a new analysis result is available. Different types of analyses may produce results at different rates, spanning different time ranges.

## Parameters

- `request`: The request that produces the result.
- `result`: The result of the analysis request.

## See Also

- [protocol SNResult](snresult.md)
  A protocol that represents sound analysis results.
- [func request(any SNRequest, didFailWithError: any Error)](snresultsobserving/request(_:didfailwitherror:).md)
  Provides any errors that occur during processing of the request.
- [func requestDidComplete(any SNRequest)](snresultsobserving/requestdidcomplete(_:).md)
  Notifies your app when the analysis request completes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresultsobserving/request(_:didproduce:))*