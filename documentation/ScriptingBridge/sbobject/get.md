# get()

**Framework**: Scripting Bridge  
**Kind**: method

Forces evaluation of the receiver, causing the real object to be returned immediately.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func get() -> Any?
```

#### Return Value

For most properties, the result is a Foundation object such as an `NSString`. For properties with no Foundation equivalent, the result is an `NSAppleEventDescriptor` or another [`SBObject`](sbobject.md) for most elements.

#### Discussion

This method forces the current object reference (the receiver) to be evaluated, resulting in the return of the referenced object. By default, Scripting Bridge deals with references to objects until you actually request some concrete data from them or until you call the `get` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbobject/get())*