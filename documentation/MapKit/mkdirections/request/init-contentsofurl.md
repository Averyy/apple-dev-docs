# init(contentsOfURL:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a directions request object using the specified URL.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(contentsOf url: URL)
```

#### Return Value

An initialized directions request object.

#### Discussion

You should use the [`isDirectionsRequest(_:)`](mkdirections/request/isdirectionsrequest(_:).md) method to verify that the specified URL is of the correct format before calling this method to initialize the object.

## Parameters

- `url`: The URL provided to your app.

## See Also

- [class func isDirectionsRequest(URL) -> Bool](mkdirections/request/isdirectionsrequest(_:).md)
  Returns a Boolean value that indicates whether the specified URL contains a directions request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/init(contentsofurl:))*