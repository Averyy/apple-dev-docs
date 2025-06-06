# setDescriptor(_:forKeyword:)

**Framework**: Foundation  
**Kind**: method

Adds a descriptor, identified by a keyword, to the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setDescriptor(_ descriptor: NSAppleEventDescriptor, forKeyword keyword: AEKeyword)
```

#### Discussion

The receiver must be an Apple event or Apple event record. Currently provides no indication if an error occurs.

## Parameters

- `descriptor`: The descriptor to add to the receiver.
- `keyword`: A keyword (a four-character code) that identifies the descriptor to add. If a descriptor with that keyword already exists in the receiver, it is replaced.

## See Also

- [func forKeyword(AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/forkeyword(_:).md)
  Returns the receiver’s descriptor for the specified keyword.
- [func keywordForDescriptor(at: Int) -> AEKeyword](nsappleeventdescriptor/keywordfordescriptor(at:).md)
  Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [func remove(withKeyword: AEKeyword)](nsappleeventdescriptor/remove(withkeyword:).md)
  Removes the receiver’s descriptor identified by the specified keyword.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/setdescriptor(_:forkeyword:))*