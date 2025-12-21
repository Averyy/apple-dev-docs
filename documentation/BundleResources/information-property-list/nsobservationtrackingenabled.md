# NSObservationTrackingEnabled

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the system automatically tracks changes to observable objects in macOS 15.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

#### Discussion

In macOS 15, add this key to your information property list and set the value to `YES` to tell the system to automatically track changes to observable objects.

In macOS 26 and later, this key isn’t required. The system automatically tracks changes to observable objects.

## See Also

- [UIObservationTrackingEnabled](information-property-list/uiobservationtrackingenabled.md)
  A Boolean value that indicates whether the system automatically tracks changes to observable objects in iOS 18.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsobservationtrackingenabled)*