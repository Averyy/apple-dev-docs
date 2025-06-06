# CancellablePromise

**Framework**: CKTool JS  
**Kind**: init

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
new inner(
	Promise inner,
	Function? cancel
);
```

## Parameters

- `inner`: 
- `cancel`: A function that takes no parameters that   uses to cancel the inner promise. If you provide this function, it must eventually throw  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/cancellablepromise)*