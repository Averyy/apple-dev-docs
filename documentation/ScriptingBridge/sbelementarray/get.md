# get()

**Framework**: Scripting Bridge  
**Kind**: method

Forces evaluation of the receiver, causing the real object to be returned immediately.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func get() -> [Any]?
```

#### Return Value

The object referenced by the receiver.

#### Discussion

This method forces the evaluation of the current object reference (the receiver), resulting in the return of the referenced object. By default, Scripting Bridge deals with references to objects until you actually request some concrete data from them or until you call the `get` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/get())*