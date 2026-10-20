# title

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A user-displayable name for the password credential to be saved.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- visionOS 26.2+

## Declaration

```swift
var title: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * title;
```

#### Discussion

This is independent of the service identifier and should be used for identifying the individual credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/assavepasswordrequest/title)*