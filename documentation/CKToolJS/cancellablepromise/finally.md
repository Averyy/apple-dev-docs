# finally

**Framework**: CKTool JS  
**Kind**: method

Tells `CancellablePromise` what callback to call when the inner promise either succeeds or fails.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise finally(
	Function? onfinally
);
```

#### Discussion

If you provide a function for the `onfinally` parameter, `CancellablePromise` calls that function after the promise succeeds or fails.

## Parameters

- `onfinally`: An optional function   calls when the inner promise succeeds or fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/finally)*