# SecTransformSetTransformAction(_:_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Changes the way that a transform deals with transform lifecycle behaviors.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformSetTransformAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ newAction: @escaping SecTransformActionBlock) -> CFError?
```

```c
extern CFErrorRefSecTransformSetTransformAction(SecTransformImplementationRef ref, CFStringRef action, SecTransformActionBlock newAction);
```

#### Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [`CFRelease`](../CoreFoundation/cfrelease.md) function to free the error’s memory when you are done with it.

## Parameters

- `ref`: A custom transform.
- `action`: The behavior to change. Valid values are [`kSecTransformActionCanExecute`](./ksectransformactioncanexecute.md), [`kSecTransformActionStartingExecution`](./ksectransformactionstartingexecution.md), [`kSecTransformActionFinalize`](./ksectransformactionfinalize.md), or [`kSecTransformActionExternalizeExtraData`](./ksectransformactionexternalizeextradata.md).
- `newAction`: A [`SecTransformActionBlock`](./sectransformactionblock.md) block that implements the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformsettransformaction(_:_:_:))*