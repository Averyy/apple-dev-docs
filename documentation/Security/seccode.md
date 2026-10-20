# SecCode

**Framework**: Security  
**Kind**: class  
**Role**: Class

A code object representing signed code running on the system.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class SecCode
```

```c
typedef struct __SecCode * SecCodeRef;
```

## Mentions

- [Hosting Guest Code](./hosting-guest-code.md)

#### Overview

In many function calls, a value of type [`SecCode`](./seccode.md) can be passed to a parameter that is typed as a [`SecStaticCode`](./secstaticcode.md). In these cases, the function performs an implicit call to the [`SecCodeCopyStaticCode(_:_:_:)`](./seccodecopystaticcode%28_,_,_%29.md) function and operates on the result.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccode)*