# isDirectionsRequest(_:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the specified URL contains a directions request.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func isDirectionsRequest(_ url: URL) -> Bool
```

```objc
+ (BOOL) isDirectionsRequestURL:(NSURL *) url;
```

## Return Value

[`true`](../../../Swift/true.md) if the URL contains a directions request that your app needs to display to the user, or [`false`](../../../Swift/false.md) if it doesn’t.

## Parameters

- `url`: The URL the system provides  to your app.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating a directions request object
- [init(contentsOfURL: URL)](./init%28contentsofurl%29.md)
  Creates and returns a directions request object using the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkdirections/request/isdirectionsrequest(_:))*