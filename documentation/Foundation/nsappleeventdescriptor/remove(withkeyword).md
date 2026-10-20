# remove(withKeyword:)

**Framework**: Foundation  
**Kind**: method

Removes the receiver’s descriptor identified by the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func remove(withKeyword keyword: AEKeyword)
```

#### Discussion

The receiver must be an Apple event or Apple event record. Currently provides no indication if an error occurs.

## Parameters

- `keyword`: A keyword (a four-character code) that identifies the descriptor to remove.

## See Also

- [func forKeyword(AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/forkeyword(_:).md)
  Returns the receiver’s descriptor for the specified keyword.
- [func keywordForDescriptor(at: Int) -> AEKeyword](nsappleeventdescriptor/keywordfordescriptor(at:).md)
  Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [func setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setdescriptor(_:forkeyword:).md)
  Adds a descriptor, identified by a keyword, to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/remove(withkeyword:))*