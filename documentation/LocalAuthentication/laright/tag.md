# tag

**Framework**: Local Authentication  
**Kind**: property

An integer you use to identify a right.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var tag: Int { get set }
```

## See Also

- [init()](laright/init.md)
  Creates a right using the default authorization requirements.
- [init(requirement: LAAuthenticationRequirement)](laright/init(requirement:).md)
  Creates a right with the authentication requirements you supply.
- [func authorize(localizedReason: String, completion: ((any Error)?) -> Void)](laright/authorize(localizedreason:completion:).md)
  Performs an authorization on the right.
- [func authorize(localizedReason: String, in: LAPresentationContext, completion: ((any Error)?) -> Void)](laright/authorize(localizedreason:in:completion:).md)
  Performs an authorization on the right with a window context you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/tag)*