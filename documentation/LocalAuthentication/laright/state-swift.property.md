# state

**Framework**: Local Authentication  
**Kind**: property  
**Role**: Instance Property

The current authorization state for a right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var state: LARight.State { get }
```

```objc
@property (nonatomic, readonly) LARightState state;
```

## See Also

### Monitoring authorization status
- [func checkCanAuthorize(completion: ((any Error)?) -> Void)](./checkcanauthorize%28completion%29.md)
  Checks whether the right has permission to perform authorization.
- [LARight.State](./state-swift.enum.md)
  The possible states for a right during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/state-swift.property)*