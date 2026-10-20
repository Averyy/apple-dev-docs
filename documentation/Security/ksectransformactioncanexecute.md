# kSecTransformActionCanExecute

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

An action that triggers to verify that all required attributes are either set or connected to another transform.

**Availability**:
- macOS 10.7+ - Deprecated in 13.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
let kSecTransformActionCanExecute: CFString
```

```c
extern CFStringRef const kSecTransformActionCanExecute;
```

#### Discussion

Overrides the standard behavior that checks to see if all of the required attributes either have been set or are connected to another transform. When overriding the default behavior the developer can decided what the necessary data is to have for a transform to be considered ‘ready to run’. Returning NULL means that the transform is ready to be run. If the transform is NOT ready to run then the override should return a CFErrorRef stipulating the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksectransformactioncanexecute)*