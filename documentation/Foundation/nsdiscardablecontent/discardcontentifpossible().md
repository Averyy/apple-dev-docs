# discardContentIfPossible()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called to discard the contents of the receiver if the value of the accessed counter is 0.

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
func discardContentIfPossible()
```

```objc
- (void) discardContentIfPossible;
```

## Discussion

This method should only discard the contents of the object if the value of the accessed counter is 0. Otherwise, it should do nothing.

## See Also

### Discarding Content
- [func isContentDiscarded() -> Bool](./iscontentdiscarded%28%29.md)
  Returns a Boolean value indicating whether the content has been discarded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/discardcontentifpossible())*