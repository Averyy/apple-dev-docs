# SecTransformFindByName(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

Finds a member of a transform group by its name.

**Availability**:
- macOS 10.7+ - Deprecated in 12.0

> **Deprecated**: SecTransform is no longer supported

## Declaration

```swift
func SecTransformFindByName(_ transform: SecGroupTransform, _ name: CFString) -> SecTransform?
```

```c
extern SecTransformRefSecTransformFindByName(SecGroupTransformRef transform, CFStringRef name);
```

#### Return Value

The transform group member, or `NULL` if the member was not found.

#### Discussion

When a transform instance is created you give it a unique name. This name can be used to find that instance in a group. While it is possible to use the [`SecTransformSetAttribute(_:_:_:_:)`](./sectransformsetattribute%28_,_,_,_%29.md) function to change a transform’s name after creating it, this is not recommended because doing so causes the [`SecTransformFindByName(_:_:)`](./sectransformfindbyname%28_,_%29.md) function to misbehave.

## Parameters

- `transform`: The transform group to be searched.
- `name`: The name of the transform to be found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformfindbyname(_:_:))*