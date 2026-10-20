# newObject()

**Framework**: AppKit  
**Kind**: method

Creates and returns a new key-value pair to represent an entry in the content dictionary.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func newObject() -> NSDictionaryControllerKeyValuePair
```

#### Return Value

An object that represents the key-value pair. The object must not be autoreleased, and must implement the NSDictionaryControllerKeyValuePair informal protocol

#### Discussion

This method is invoked for insertions of new key-value pairs, as well as transforming existing dictionary entries into key-value pairs for display. Objects returned by this method must implement the NSDictionaryControllerKeyValuePair informal protocol.

##### Special Considerations

Subclass implementations must ensure that the object returned by `newObject` is not autoreleased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdictionarycontroller/newobject())*