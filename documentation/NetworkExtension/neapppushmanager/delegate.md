# delegate

**Framework**: Network Extension  
**Kind**: property

A delegate that receives incoming call information from the provider.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any NEAppPushDelegate)? { get set }
```

## See Also

- [protocol NEAppPushDelegate](neapppushdelegate.md)
  A protocol that defines how an app push manager instance interacts with the framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/delegate)*