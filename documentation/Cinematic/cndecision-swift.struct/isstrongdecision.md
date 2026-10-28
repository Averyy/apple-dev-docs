# isStrongDecision

**Framework**: Cinematic  
**Kind**: property  
**Role**: Instance Property

A flag representing whether this is a strong decision.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var isStrongDecision: Bool { get }
```

## Discussion

A strong decision keeps focus for as long as possible on the detected subject.

## See Also

### Instance Properties
- [var focusDetectionID: CNDecision.FocusDetectionID](./focusdetectionid-swift.property.md)
- [var isUserDecision: Bool](./isuserdecision.md)
  A flag representing whether this is a user-created decision or a base decision.
- [var time: CMTime](./time.md)
  The first presentation time that the subject should be in focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndecision-swift.struct/isstrongdecision)*