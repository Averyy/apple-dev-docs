# init(identifier:)

**Framework**: Game Controller  
**Kind**: init  
**Role**: Initializer

Create a device type for an identifier.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
convenience init?(identifier: String)
```

```objc
+ (instancetype) deviceTypeWithIdentifier:(NSString *) identifier;
```

#### Discussion

This initializer returns nil if the system doesn’t know the device type for \a identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicetype/init(identifier:))*