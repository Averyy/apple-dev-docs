# request(_:didFailWithError:)

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

Provides any errors that occur during processing of the request.

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
optional func request(_ request: any SNRequest, didFailWithError error: any Error)
```

```objc
- (void) request:(id<SNRequest>) request didFailWithError:(NSError *) error;
```

#### Discussion

The analyzer stops processing a specific request when it encounters an error, and doesn’t call [`requestDidComplete(_:)`](./requestdidcomplete%28_%29.md).

## Parameters

- `request`: The request that produces the error.
- `error`: The error that occurs during the request.

## See Also

### Handling Requests
- [func request(any SNRequest, didProduce: any SNResult)](./request%28_,didproduce%29.md)
  Provides a new analysis result to your app with the specified time range.
- [protocol SNResult](../snresult.md)
  A protocol that represents sound analysis results.
- [func requestDidComplete(any SNRequest)](./requestdidcomplete%28_%29.md)
  Notifies your app when the analysis request completes normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snresultsobserving/request(_:didfailwitherror:))*