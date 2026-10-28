# UIObservationTrackingEnabled

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the system automatically tracks changes to observable objects in iOS 18.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Details

- **Name**: `UIObservationTrackingEnabled`
- **Type**: boolean

## Discussion

In iOS 18, add this key to your information property list and set the value to `YES` to tell the system to automatically track changes to observable objects.

In iOS 26 and later, this key isn’t required. The system automatically tracks changes to observable objects.

## See Also

### Automatic observation tracking
- [NSObservationTrackingEnabled](./nsobservationtrackingenabled.md)
  A Boolean value that indicates whether the system automatically tracks changes to observable objects in macOS 15.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uiobservationtrackingenabled)*