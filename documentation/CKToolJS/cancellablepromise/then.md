# then

**Framework**: CKTool JS  
**Kind**: method

Tells `CancellablePromise` what callbacks to call on success or failure of the inner promise.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise then(
	Function? onrejected,
	Function? onfullfilled
);
```

#### Discussion

If you provide a function for the `onrejected` parameter, `CancellablePromise` will call that function if the promise fails.

If you provide a function for the `onfulfilled` parameter, `CancellablePromise` will call that function if the promise succeeds.

## Parameters

- `onrejected`: An optional function   calls when the inner promise rejects.
- `onfullfilled`: An optional function   calls when the inner promise resolves successfully.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/then)*