# maximumAllowedAgeRating

**Framework**: MarketplaceKit  
**Kind**: property

An age rating that specifies the maximum rating set for content on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@MainActor
final var maximumAllowedAgeRating: Int { get }
```

## Mentions

- [Providing age-rating appropriate content](providing-age-rating-appropriate-content.md)

#### Discussion

The framework derives the value of this property according to the restrictions set on the device.

The value is a code that maps to the following age ratings:

| Return value | Rating |
| --- | --- |
| 1 | 1+ |
| 2 | 2+ |
| 3 | 3+ |
| 100 | 4+ |
| 105 | 5+ |
| 106 | 6+ |
| 107 | 7+ |
| 108 | 8+ |
| 200 | 9+ |
| 210 | 10+ |
| 211 | 11+ |
| 300 | 12+ |
| 313 | 13+ |
| 314 | 14+ |
| 415 | 15+ |
| 416 | 16+ |
| 600 | 17+ |
| 618 | 18+ |
| 619 | 19+ |
| 620 | 20+ |
| 621 | 21+ |
| 2000 | Unrated |

## See Also

- [AppLibrary.ExceptionRequest](applibrary/exceptionrequest.md)
  A structure that describes an app that a person requests permission to install.
- [func currentAgeExceptionRequests() async throws -> [AppLibrary.ExceptionRequest]](applibrary/currentageexceptionrequests.md)
  Returns a list of requests to install apps that exceed the maximum allowed age rating for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/marketplacekit/applibrary/maximumallowedagerating)*