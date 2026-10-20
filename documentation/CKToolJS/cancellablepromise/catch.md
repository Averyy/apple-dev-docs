# catch

**Framework**: CKTool JS  
**Kind**: method  
**Role**: Instance Method

Tells `CancellablePromise` what callback to call on failure of the inner promise.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
CancellablePromise catch(
	Function? onrejected
);
```

#### Discussion

If you provide a function for the `onrejected` parameter, `CancellablePromise` calls that function if the promise fails.

## Parameters

- `onrejected`: An optional function `CancellablePromise` calls when the inner promise rejects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/catch)*