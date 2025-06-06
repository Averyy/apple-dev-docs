# UIApplication.CategoryDefaultError.Code

**Framework**: UIKit  
**Kind**: enum

An enumeration of reasons an error happens when the system discovers whether your app is the default in a category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [UIApplication.CategoryDefaultError.Code.rateLimited](uiapplication/categorydefaulterror/code/ratelimited.md)
  The system didn’t determine if your app is the default in a category because the app made the request too many times.
### Initializers
- [init?(rawValue: Int)](uiapplication/categorydefaulterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static let retryAvailableDateErrorKey: String](uiapplication/categorydefaulterror/retryavailabledateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [static let statusLastProvidedDateErrorKey: String](uiapplication/categorydefaulterror/statuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror/code)*