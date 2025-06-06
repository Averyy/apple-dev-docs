# state

**Framework**: Local Authentication  
**Kind**: property

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

## See Also

- [func checkCanAuthorize(completion: ((any Error)?) -> Void)](laright/checkcanauthorize(completion:).md)
  Checks whether the right has permission to perform authorization.
- [LARight.State](laright/state-swift.enum.md)
  The possible states for a right during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/state-swift.property)*