# limit

**Framework**: MusicKit  
**Kind**: property

A limit for the number of items to return in the library search response.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var limit: Int
```

#### Discussion

The default value for this limit is 50.

If the application sets the limit to 0, the framework returns all matching items in the user’s music library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musiclibrarysearchrequest/limit)*