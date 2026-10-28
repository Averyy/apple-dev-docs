# cancel()

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Cancels a pending request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func cancel()
```

```objc
- (void) cancel;
```

## Discussion

After canceling a request, you can call the [`calculate(completionHandler:)`](./calculate%28completionhandler%29.md) method again (if you want) to restart the request process.

## See Also

### Managing the request
- [var isCalculating: Bool](./iscalculating.md)
  A Boolean value that indicates whether a request is in process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/cancel())*