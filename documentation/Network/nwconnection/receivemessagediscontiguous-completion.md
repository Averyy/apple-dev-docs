# receiveMessageDiscontiguous(completion:)

**Framework**: Network  
**Kind**: method

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@preconcurrency
final func receiveMessageDiscontiguous(completion: @escaping (DispatchData?, NWConnection.ContentContext?, Bool, NWError?) -> Void)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwconnection/receivemessagediscontiguous(completion:))*