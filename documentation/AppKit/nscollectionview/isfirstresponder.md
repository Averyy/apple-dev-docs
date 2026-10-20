# isFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the collection view is the first responder.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var isFirstResponder: Bool { get }
```

```objc
@property (readonly, getter=isFirstResponder) BOOL firstResponder;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the collection view is the first responder. This property is fully key-value observing compliant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionview/isfirstresponder)*