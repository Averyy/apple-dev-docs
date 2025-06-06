# catch

**Framework**: CKTool JS  
**Kind**: method

Tells `CancellablePromise` what callback to call on failure of the inner promise.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
CancellablePromise catch(
	Function? onrejected
);
```

#### Discussion

If you provide a function for the `onrejected` parameter, `CancellablePromise` calls that function if the promise fails.

## Parameters

- `onrejected`: An optional function   calls when the inner promise rejects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cancellablepromise/catch)*