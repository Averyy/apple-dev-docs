# signal

**Framework**: MapKit JS  
**Kind**: property

A signal object allowing you to cancel the request.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
signal?: AbortSignal;
```

#### Discussion

Pass an `AbortSignal` from an `AbortController` to allow the controller to cancel a pending reverse geocoder lookup request. When the controller aborts, the promise it returns rejects with a `DOMException` whose `name` is `"AbortError"`.

## See Also

- [language](geocoderreverselookupoptions/language.md)
  The language to use when displaying the reverse lookup results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/geocoderreverselookupoptions/signal)*