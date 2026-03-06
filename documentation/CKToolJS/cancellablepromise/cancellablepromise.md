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
- `cancel`: The optional function you can use to cancel the promise. A function that takes no parameters that `CancellablePromise` uses to cancel the inner promise. If you provide this function, it must eventually throw `CancelledError`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/cancellablepromise)*