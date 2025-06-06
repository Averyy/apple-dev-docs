# activate()

**Framework**: Dispatch  
**Kind**: method

Activates the dispatch object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func activate()
```

#### Discussion

Once a dispatch object has been activated, it cannot change its target queue.

## See Also

- [func resume()](dispatchobject/resume.md)
  Resumes the invocation of block objects on a dispatch object.
- [func suspend()](dispatchobject/suspend.md)
  Suspends the invocation of block objects on a dispatch object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchobject/activate())*