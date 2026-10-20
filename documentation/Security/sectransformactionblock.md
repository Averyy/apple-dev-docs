# SecTransformActionBlock

**Framework**: Security  
**Kind**: typealias  
**Role**: Type Alias

A block that overrides the default behavior of a custom transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
typealias SecTransformActionBlock = () -> Unmanaged<CFTypeRef>?
```

```c
typedef const void *(^)(void) SecTransformActionBlock;
```

#### Return Value

A dictionary of the custom items to be exported if this block is used to override the [`kSecTransformActionExternalizeExtraData`](./ksectransformactionexternalizeextradata.md) action or  `NULL` for any other action. Alternatively, the block returns a [`CFError`](../CoreFoundation/cferror.md) object if an error occurs.

#### Discussion

A  block of this type is used to override the default behavior of a custom transform. This block is associated with the SecTransformOverrideTransformAction block.

The behaviors that can be overridden are:

- [`kSecTransformActionCanExecute`](./ksectransformactioncanexecute.md) - Determine if the transform has all of the data needed to run.
- [`kSecTransformActionStartingExecution`](./ksectransformactionstartingexecution.md) - Called just before running ProcessData.
- [`kSecTransformActionFinalize`](./ksectransformactionfinalize.md) - Called just before deleting the custom transform.
- [`kSecTransformActionExternalizeExtraData`](./ksectransformactionexternalizeextradata.md) - Called to allow for writing out custom data to be exported.

For example:

```objc
SecTransformImplementationRef ref;
CFErrorRef error = NULL;
 
error = SecTransformSetTransformAction(ref, kSecTransformActionStartingExecution, ^{
    // Initialize any data needed before running
    CFErrorRef result = DoMyInitialization();
    return result;});
 
SecTransformTransformActionBlock actionBlock =
^{
    // Clean up any existing data before running
    CFErrorRef result = DoMyFinalization();
    return result;};
 
error = SecTransformSetTransformAction(ref, kSecTransformActionFinalize,actionBlock);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformactionblock)*