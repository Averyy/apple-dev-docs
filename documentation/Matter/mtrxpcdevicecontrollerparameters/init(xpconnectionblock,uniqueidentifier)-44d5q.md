# init(xpConnectionBlock:uniqueIdentifier:)

**Framework**: Matter  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.2+ - Deprecated in 26.0
- iPadOS 18.2+ - Deprecated in 26.0
- Mac Catalyst 18.2+ - Deprecated in 26.0
- macOS 15.2+ - Deprecated in 26.0
- tvOS 18.2+ - Deprecated in 26.0
- visionOS 2.2+ - Deprecated in 26.0
- watchOS 11.2+ - Deprecated in 26.0

> **Deprecated**: Please use initWithXPCConnectionBlock:uniqueIdentifier:

## Declaration

```swift
init(xpConnectionBlock xpcConnectionBlock: @escaping () -> NSXPCConnection, uniqueIdentifier: UUID)
```

```objc
- (instancetype) initWithXPConnectionBlock:(NSXPCConnection * (^)()) xpcConnectionBlock uniqueIdentifier:(NSUUID *) uniqueIdentifier;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrxpcdevicecontrollerparameters/init(xpconnectionblock:uniqueidentifier:)-44d5q)*