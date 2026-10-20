# displayName

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

The display name for this peer.

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
var displayName: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSString * displayName;
```

*macOS*

```objc
@property (atomic, readonly) NSString * displayName;
```

#### Discussion

For the local peer, you set this property when the object is initialized. It cannot be changed.

For other peer objects provided to you by the framework, this property is provided by the peer and cannot be changed.

## See Also

### Peer Methods
- [init(displayName: String)](./init%28displayname%29.md)
  Initializes a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/displayname)*