# name

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The name of the user.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

#### Discussion

User names must be unique.

## See Also

### Related Documentation
- [HomeKit Developer Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/HomeKitDeveloperGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40015050)
### Getting Information About the User
- [var uniqueIdentifier: UUID](./uniqueidentifier.md)
  A unique identifier for the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmuser/name)*