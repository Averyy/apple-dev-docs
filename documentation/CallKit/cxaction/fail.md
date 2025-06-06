# fail()

**Framework**: CallKit  
**Kind**: method

Reports the failed execution of the action.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func fail()
```

#### Discussion

Calling this method sets the [`isComplete`](cxaction/iscomplete.md) property value to [`true`](https://developer.apple.com/documentation/swift/true). Calling this method more than once or calling it after calling the [`fulfill()`](cxaction/fulfill().md) method has no effect.

You should only call this method from the implementation of a `CXProviderDelegate` method.

## See Also

- [func fulfill()](cxaction/fulfill.md)
  Reports the successful execution of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxaction/fail())*