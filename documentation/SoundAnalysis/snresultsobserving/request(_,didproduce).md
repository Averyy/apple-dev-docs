# request(_:didProduce:)

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) request:(id<SNRequest>) request didProduceResult:(id<SNResult>) result;
```

#### Discussion

The analyzer calls this function each time a new analysis result is available. Different types of analyses may produce results at different rates, spanning different time ranges.

## Parameters

- `request`: The request that produces the result.
- `result`: The result of the analysis request.

## See Also

### Handling Requests
- [protocol SNResult](../snresult.md)
  A protocol that represents sound analysis results.
- [func request(any SNRequest, didFailWithError: any Error)](./request%28_,didfailwitherror%29.md)
  Provides any errors that occur during processing of the request.
- [func requestDidComplete(any SNRequest)](./requestdidcomplete%28_%29.md)
  Notifies your app when the analysis request completes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresultsobserving/request(_:didproduce:))*