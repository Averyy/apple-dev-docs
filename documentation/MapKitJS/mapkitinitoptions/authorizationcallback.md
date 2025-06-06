# authorizationCallback

**Framework**: MapKit JS  
**Kind**: method

A callback function that obtains a token.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
void authorizationCallback(
	function done
);
```

#### Discussion

MapKit JS asyncronously invokes the `authorizationCallback` function throughout a session to obtain new authorization tokens. In the callback, you create a token and pass it to the function that MapKit JS provides in the `done` parameter.

## Parameters

- `done`: A function that completes the MapKit JS token request. Called after creating a new token.

## See Also

- [language](mapkitinitoptions/language.md)
  An ID that indicates the preferred language to use when displaying map labels, controls, directions, and other text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitinitoptions/authorizationcallback)*