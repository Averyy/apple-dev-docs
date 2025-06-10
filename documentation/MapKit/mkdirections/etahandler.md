# MKDirections.ETAHandler

**Framework**: MapKit  
**Kind**: typealias

The block to use for processing travel-time information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias ETAHandler = (MKDirections.ETAResponse?, (any Error)?) -> Void
```

#### Discussion

The implementation of your block needs to check for a value in the `error` parameter and, if that parameter is `nil`, incorporate the travel-time information from the `response` parameter.

## Parameters

- `response`: The   parameter contains the travel-time response. If an error occurs or the framework can’t determine the travel time, this parameter is  .
- `error`: The   parameter contains information about any errors that occur. If no errors occur, this parameter is  .

## See Also

- [func calculateETA(completionHandler: (MKDirections.ETAResponse?, (any Error)?) -> Void)](mkdirections/calculateeta(completionhandler:).md)
  Begins calculating the requested travel-time information asynchronously.
- [MKDirections.ETAResponse](mkdirections/etaresponse.md)
  The travel-time information that Apple servers return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/etahandler)*