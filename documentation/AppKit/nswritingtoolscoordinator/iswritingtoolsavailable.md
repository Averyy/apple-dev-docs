# isWritingToolsAvailable

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A Boolean value that indicates whether Writing Tools features are available to enable.

**Availability**:
- macOS 15.2+

## Declaration

```swift
class var isWritingToolsAvailable: Bool { get }
```

```objc
@property (class, readonly) BOOL isWritingToolsAvailable;
```

## Discussion

The value of this property is `true` when Writing Tools features are supported, even when the user has not enabled the feature. Writing Tools support might be unavailable because of device constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/iswritingtoolsavailable)*