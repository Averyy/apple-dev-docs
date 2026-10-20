# session

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A contract to declare an AR session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var session: ARSession { get }
```

```objc
@property (readonly) ARSession * session;
```

#### Discussion

Some clients may use key-value observation (KVO) to be notified when this property changes values. To support KVO, Swift classes that adopt [`ARSessionProviding`](../arsessionproviding.md) should mark its [`session`](./session.md) as `@objc` and `dynamic`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsessionproviding/session)*