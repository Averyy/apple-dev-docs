# location

**Framework**: Core Location  
**Kind**: property

The most recently retrieved user location.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var location: CLLocation? { get }
```

#### Discussion

The value of this property is `nil` if no location data has ever been retrieved.

In iOS 4.0 and later, this property may contain a more recent location object at launch time. Specifically, if significant location updates are running and your app is terminated, this property is updated with the most recent location data when your app is relaunched (and you create a new location manager object). This location data may be more recent than the last location event processed by your app.

It is always a good idea to check the timestamp of the location stored in this property. If the receiver is currently gathering location data, but the minimum distance filter is large, the returned location might be relatively old. If it is, you can stop the receiver and start it again to force an update.

## Topics

### Related Documentation
- [func startUpdatingLocation()](cllocationmanager/startupdatinglocation.md)
  Starts the generation of updates that report the user’s current location.

## See Also

- [var heading: CLHeading?](cllocationmanager/heading.md)
  The most recently reported heading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/location)*