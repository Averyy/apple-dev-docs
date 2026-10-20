# init(requirement:)

**Framework**: Local Authentication  
**Kind**: init  
**Role**: Initializer

Creates a right with the authentication requirements you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(requirement: LAAuthenticationRequirement)
```

```objc
- (instancetype) initWithRequirement:(LAAuthenticationRequirement *) requirement;
```

## See Also

### Authorizing a right
- [init()](./init%28%29.md)
  Creates a right using the default authorization requirements.
- [var tag: Int](./tag.md)
  An integer you use to identify a right.
- [func authorize(localizedReason: String, completion: ((any Error)?) -> Void)](./authorize%28localizedreason,completion%29.md)
  Performs an authorization on the right.
- [func authorize(localizedReason: String, in: LAPresentationContext, completion: ((any Error)?) -> Void)](./authorize%28localizedreason,in,completion%29.md)
  Performs an authorization on the right with a window context you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/init(requirement:))*