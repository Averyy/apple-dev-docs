# remove(withKeyword:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Removes the receiver’s descriptor identified by the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func remove(withKeyword keyword: AEKeyword)
```

```objc
- (void) removeDescriptorWithKeyword:(AEKeyword) keyword;
```

#### Discussion

The receiver must be an Apple event or Apple event record. Currently provides no indication if an error occurs.

## Parameters

- `keyword`: A keyword (a four-character code) that identifies the descriptor to remove.

## See Also

### Working With Record Descriptors
- [func forKeyword(AEKeyword) -> NSAppleEventDescriptor?](./forkeyword%28_%29.md)
  Returns the receiver’s descriptor for the specified keyword.
- [func keywordForDescriptor(at: Int) -> AEKeyword](./keywordfordescriptor%28at%29.md)
  Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [func setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)](./setdescriptor%28_,forkeyword%29.md)
  Adds a descriptor, identified by a keyword, to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/remove(withkeyword:))*