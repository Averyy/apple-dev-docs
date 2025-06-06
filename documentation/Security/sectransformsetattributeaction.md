# SecTransformSetAttributeAction(_:_:_:_:)

**Framework**: Security  
**Kind**: func

Requests a callback when an attribute is set.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformSetAttributeAction(_ ref: SecTransformImplementationRef, _ action: CFString, _ attribute: SecTransformStringOrAttribute?, _ newAction: @escaping SecTransformAttributeActionBlock) -> CFError?
```

#### Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) function to free the error’s memory when you are done with it.

#### Discussion

The [`kSecTransformActionProcessData`](ksectransformactionprocessdata.md) action used with the [`SecTransformSetDataAction(_:_:_:)`](sectransformsetdataaction(_:_:_:).md) function is a special case of a [`SecTransformSetAttributeAction(_:_:_:_:)`](sectransformsetattributeaction(_:_:_:_:).md) action. If this is called on the input attribute then it will overwrite any [`kSecTransformActionProcessData`](ksectransformactionprocessdata.md) action.

You may call this function multiple times for either a named attribute or for all attributes when the attribute parameter is `NULL`. The last call takes precedence.

## Parameters

- `ref`: A   that is bound to an instance of a custom transform.
- `action`: Use   to add a block that is called to validate the input to an attribute.
- `attribute`: The name of the attribute that will be handled. An attribute reference may also be given here. A   value indicates that the supplied action is for all attributes.
- `newAction`: A   which implements the behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformsetattributeaction(_:_:_:_:))*