# BEAvailability.Context

**Framework**: BrowserKit  
**Kind**: enum  
**Role**: Enumeration

The category of app for which you determine eligibility.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
enum Context
```

```c
enum BEEligibilityContext : NSInteger;
```

## Topics

### Identifying app contexts
- [BEAvailability.Context.webBrowser](./context/webbrowser.md)
  The app is a web browser.
### Initializing an availability object
- [init?(rawValue: Int)](./context/init%28rawvalue%29.md)
  Creates a new context with the given value of the underlying type.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beavailability/context)*