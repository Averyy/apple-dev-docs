# MKDirections.DirectionsHandler

**Framework**: MapKit  
**Kind**: typealias

The block to use for processing the requested route information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias DirectionsHandler = (MKDirections.Response?, (any Error)?) -> Void
```

#### Discussion

The implementation of your block needs to check for a value in the `error` parameter and, if that parameter is `nil`, incorporate the route information from the `response` parameter.

## Parameters

- `response`: The   parameter contains the route information for the request. If an error occurs or the framework can’t determine a route, this parameter is  .
- `error`: The   parameter contains information about any errors that occur. If no errors occur, this parameter is  .

## See Also

- [func calculate(completionHandler: MKDirections.DirectionsHandler)](mkdirections/calculate(completionhandler:).md)
  Begins calculating the requested route information asynchronously.
- [MKDirections.Response](mkdirections/response.md)
  The route information that Apple servers return in response to your request for directions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/directionshandler)*