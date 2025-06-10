# authorize(localizedReason:in:completion:)

**Framework**: Local Authentication  
**Kind**: method

Performs an authorization on the right with a window context you supply.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func authorize(localizedReason: String, in presentationContext: LAPresentationContext) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func authorize(localizedReason: String, in presentationContext: LAPresentationContext) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## See Also

- [init()](laright/init.md)
  Creates a right using the default authorization requirements.
- [init(requirement: LAAuthenticationRequirement)](laright/init(requirement:).md)
  Creates a right with the authentication requirements you supply.
- [var tag: Int](laright/tag.md)
  An integer you use to identify a right.
- [func authorize(localizedReason: String, completion: ((any Error)?) -> Void)](laright/authorize(localizedreason:completion:).md)
  Performs an authorization on the right.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/authorize(localizedreason:in:completion:))*