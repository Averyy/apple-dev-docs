# SecTransformPushbackAttribute(_:_:_:)

**Framework**: Security  
**Kind**: func

Pushes a single value back for a specific attribute.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecTransformPushbackAttribute(_ ref: SecTransformImplementationRef, _ attribute: SecTransformStringOrAttribute, _ value: CFTypeRef) -> CFTypeRef?
```

#### Return Value

An error on failure, or `NULL` on success. In Objective-C, call the [`CFRelease`](https://developer.apple.com/documentation/CoreFoundation/CFRelease) function to free the error’s memory when you are done with it.

#### Discussion

Calling this function stops the flow of data into the specified attribute until any attribute is changed for the transform instance bound to the `ref` parameter.

## Parameters

- `ref`: A   that is bound to an instance of a custom transform.
- `attribute`: The name or the attribute handle of the attribute whose value is to be pushed back. When using a name, see   for a list of valid key names.
- `value`: The value being pushed back.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectransformpushbackattribute(_:_:_:))*