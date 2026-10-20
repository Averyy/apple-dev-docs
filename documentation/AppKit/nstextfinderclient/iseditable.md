# isEditable

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns whether the text is editable.

**Availability**:
- macOS

## Declaration

```swift
optional var isEditable: Bool { get }
```

```objc
@property (readonly, getter=isEditable) BOOL editable;
```

#### Discussion

The text finder uses this property to validate actions. If is it not implemented, the value is assumed to be [`true`](../../Swift/true.md) .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfinderclient/iseditable)*