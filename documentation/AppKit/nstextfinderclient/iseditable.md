# isEditable

**Framework**: AppKit  
**Kind**: property

Returns whether the text is editable.

**Availability**:
- macOS ?+

## Declaration

```swift
optional var isEditable: Bool { get }
```

#### Discussion

The text finder uses this property to validate actions. If is it not implemented, the value is assumed to be [`true`](https://developer.apple.com/documentation/swift/true) .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/iseditable)*