# serviceType

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The service type that your app is advertising.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
var serviceType: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSString * serviceType;
```

*macOS*

```objc
@property (atomic, readonly) NSString * serviceType;
```

## Discussion

You set this property’s value when you initialize the object. It cannot be changed later.

## See Also

### Initializing and Configuring
- [init(serviceType: String, discoveryInfo: [String : String]?, session: MCSession)](./init%28servicetype,discoveryinfo,session%29.md)
  Initializes an advertiser assistant object.
- [var session: MCSession](./session.md)
  The session into which new peers are added after accepting an invitation.
- [var delegate: (any MCAdvertiserAssistantDelegate)?](./delegate.md)
  The delegate object that handles advertising-assistant-related events.
- [var discoveryInfo: [String : String]?](./discoveryinfo.md)
  The `info` dictionary that was passed when this object was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/servicetype)*