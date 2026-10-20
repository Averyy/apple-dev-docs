# expiresDate

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The cookie’s expiration date.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var expiresDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * expiresDate;
```

#### Discussion

This value is `nil` if there is no specific expiration date, as with session-only cookies. The expiration date is the date when the cookie should be deleted.

## See Also

### Determining cookie lifespan
- [var isSessionOnly: Bool](./issessiononly.md)
  A Boolean value that indicates whether the cookie should be discarded at the end of the session (regardless of expiration date).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/expiresdate)*