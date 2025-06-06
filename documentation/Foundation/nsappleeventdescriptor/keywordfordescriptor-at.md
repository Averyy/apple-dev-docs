# keywordForDescriptor(at:)

**Framework**: Foundation  
**Kind**: method

Returns the keyword for the descriptor at the specified (one-based) position in the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func keywordForDescriptor(at index: Int) -> AEKeyword
```

#### Return Value

The keyword (a four-character code) for the descriptor at the one-based location specified by `anIndex`, or 0 if an error occurs.

## Parameters

- `index`: The one-based descriptor list position of the descriptor to get the keyword for.

## See Also

- [func forKeyword(AEKeyword) -> NSAppleEventDescriptor?](nsappleeventdescriptor/forkeyword(_:).md)
  Returns the receiver’s descriptor for the specified keyword.
- [func remove(withKeyword: AEKeyword)](nsappleeventdescriptor/remove(withkeyword:).md)
  Removes the receiver’s descriptor identified by the specified keyword.
- [func setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setdescriptor(_:forkeyword:).md)
  Adds a descriptor, identified by a keyword, to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/keywordfordescriptor(at:))*