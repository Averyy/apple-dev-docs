# endContentAccess()

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Called if the discardable contents are no longer being accessed.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func endContentAccess()
```

#### Discussion

This method decrements the counter variable of the object, which will usually bring the value of the counter variable back down to 0, which allows the discardable contents of the object to be thrown away if necessary.

## See Also

- [func beginContentAccess() -> Bool](nsdiscardablecontent/begincontentaccess.md)
  Returns a Boolean value indicating whether the discardable contents are still available and have been successfully accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/endcontentaccess())*