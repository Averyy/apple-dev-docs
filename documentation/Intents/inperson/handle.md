# handle

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The unique identifier that your app assigned to the user.

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.12
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use personHandle instead

## Declaration

```swift
var handle: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * handle;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * handle;
```

## Discussion

The value of this property is the string that you specified at initialization time. Use this string to identify the user uniquely in your app. For example, you might specify an email address, phone number, or account name associated with the user. Siri may show this string when asking the user to choose from among several people with similar names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/handle)*