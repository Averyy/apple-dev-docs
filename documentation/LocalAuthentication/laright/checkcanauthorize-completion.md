# checkCanAuthorize(completion:)

**Framework**: Local Authentication  
**Kind**: method

Checks whether the right has permission to perform authorization.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func checkCanAuthorize() async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func checkCanAuthorize() async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func checkCanAuthorize() async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

## Parameters

- `handler`: A completion handler called when the authorization check finishes.

## See Also

- [var state: LARight.State](laright/state-swift.property.md)
  The current authorization state for a right.
- [LARight.State](laright/state-swift.enum.md)
  The possible states for a right during authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/localauthentication/laright/checkcanauthorize(completion:))*