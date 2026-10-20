# isContentDiscarded()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a Boolean value indicating whether the content has been discarded.

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
func isContentDiscarded() -> Bool
```

```objc
- (BOOL) isContentDiscarded;
```

#### Return Value

[`true`](../../Swift/true.md) if the content has been discarded; otherwise, [`false`](../../Swift/false.md).

## See Also

### Discarding Content
- [func discardContentIfPossible()](./discardcontentifpossible%28%29.md)
  Called to discard the contents of the receiver if the value of the accessed counter is 0.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdiscardablecontent/iscontentdiscarded())*