# code

**Framework**: MapKit JS  
**Kind**: property

The code indicating why location acquisition failed.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
readonly code: number;
```

#### Discussion

The error codes mirror the HTML Geolocation API’s error codes with one additional MapKit JS-specific error code:

- **`Error.PERMISSION_DENIED` (`1`)**: The user refuses permission to obtain location information.
- **`Error.POSITION_UNAVAILABLE` (`2`)**: The Geolocation API returns an error.
- **`Error.TIMEOUT` (`3`)**: The operation times out without acquiring the location.
- **`Error.MAPKIT_NOT_INITIALIZED` (`4`)**: MapKit JS isn’t initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapuserlocationerrorevent/code)*