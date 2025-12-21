# beginContentAccess()

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Returns a Boolean value indicating whether the discardable contents are still available and have been successfully accessed.

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
func beginContentAccess() -> Bool
```

#### Return Value

YES if the discardable contents are still available and have now been successfully accessed; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

Call this method if the object’s memory is needed or is about to be used. This method increments the counter variable, thus protecting the object’s memory from possibly being discarded. The implementing class may decide that this method will try to recreate the contents if they have been discarded and return YES if the re-creation was successful. Implementors of this protocol should raise exceptions if the `NSDiscardableContent` objects are used when the `beginContentAccess` method has not been called on them.

## See Also

- [func endContentAccess()](nsdiscardablecontent/endcontentaccess.md)
  Called if the discardable contents are no longer being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/begincontentaccess())*