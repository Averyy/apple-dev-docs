# cancel()

**Framework**: MapKit  
**Kind**: method

Cancels a pending request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
func cancel()
```

#### Discussion

After canceling a request, you can call the [`calculate(completionHandler:)`](mkdirections/calculate(completionhandler:).md) method again (if you want) to restart the request process.

## See Also

- [var isCalculating: Bool](mkdirections/iscalculating.md)
  A Boolean value that indicates whether a request is in process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/cancel())*