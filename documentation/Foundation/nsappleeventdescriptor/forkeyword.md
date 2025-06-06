# forKeyword(_:)

**Framework**: Foundation  
**Kind**: method

Returns the receiver’s descriptor for the specified keyword.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func forKeyword(_ keyword: AEKeyword) -> NSAppleEventDescriptor?
```

#### Return Value

A descriptor for the specified keyword, or `nil` if an error occurs.

## Parameters

- `keyword`: A keyword (a four-character code) that identifies the descriptor to obtain.

## See Also

- [func keywordForDescriptor(at: Int) -> AEKeyword](nsappleeventdescriptor/keywordfordescriptor(at:).md)
  Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [func remove(withKeyword: AEKeyword)](nsappleeventdescriptor/remove(withkeyword:).md)
  Removes the receiver’s descriptor identified by the specified keyword.
- [func setDescriptor(NSAppleEventDescriptor, forKeyword: AEKeyword)](nsappleeventdescriptor/setdescriptor(_:forkeyword:).md)
  Adds a descriptor, identified by a keyword, to the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/forkeyword(_:))*