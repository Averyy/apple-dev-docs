# authorizationCallback

**Framework**: MapKit JS  
**Kind**: property

A callback function that obtains a token.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
authorizationCallback?: (this: null, done: (token: string) => void) => void;
```

#### Discussion

MapKit JS asyncronously invokes the `authorizationCallback` function throughout a session to obtain new authorization tokens. In the callback, you create a token and pass it to the function that MapKit JS provides in the `done` parameter.

## Parameters

- `done`: A function that completes the MapKit JS token request, called after creating a new token.

## See Also

- [language](mapkitinitializationoptions/language.md)
  An ID that indicates the preferred language to use when displaying map labels, controls, directions, and other text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitinitializationoptions/authorizationcallback)*