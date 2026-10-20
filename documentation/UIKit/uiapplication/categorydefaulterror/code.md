# UIApplication.CategoryDefaultError.Code

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of reasons an error happens when the system discovers whether your app is the default in a category.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+

## Declaration

```swift
enum Code
```

```c
enum UIApplicationCategoryDefaultErrorCode : NSInteger;
```

## Topics

### Error codes
- [UIApplication.CategoryDefaultError.Code.rateLimited](./code/ratelimited.md)
  The system didn’t determine if your app is the default in a category because the app made the request too many times.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Getting information about the error
- [static let retryAvailableDateErrorKey: String](./retryavailabledateerrorkey.md)
  A dictionary key, with a value that’s a date when a result is next available.
- [static let statusLastProvidedDateErrorKey: String](./statuslastprovideddateerrorkey.md)
  A dictionary key, with a value that’s the date your app last received a successful result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror/code)*