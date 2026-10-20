# NSObservationTrackingEnabled

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the system automatically tracks changes to observable objects in macOS 15.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Details

- **Name**: `NSObservationTrackingEnabled`
- **Type**: boolean

#### Discussion

In macOS 15, add this key to your information property list and set the value to `YES` to tell the system to automatically track changes to observable objects.

In macOS 26 and later, this key isn’t required. The system automatically tracks changes to observable objects.

## See Also

### Automatic observation tracking
- [UIObservationTrackingEnabled](./uiobservationtrackingenabled.md)
  A Boolean value that indicates whether the system automatically tracks changes to observable objects in iOS 18.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsobservationtrackingenabled)*