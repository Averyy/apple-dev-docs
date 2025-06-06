# unbind(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Removes a given binding between the receiver and a controller.

**Availability**:
- macOS ?+

## Declaration

```swift
func unbind(_ binding: NSBindingName)
```

## Parameters

- `binding`: The name of a binding.

## See Also

- [func valueClassForBinding(NSBindingName) -> AnyClass?](nsobject-swift.class/valueclassforbinding(_:).md)
  Returns the class of the value that will be returned for the specified binding.
- [func bind(NSBindingName, to: Any, withKeyPath: String, options: [NSBindingOption : Any]?)](nsobject-swift.class/bind(_:to:withkeypath:options:).md)
  Establishes a binding between a given property of the receiver and the property of a given object specified by a given key path.
- [func optionDescriptionsForBinding(NSBindingName) -> [NSAttributeDescription]](nsobject-swift.class/optiondescriptionsforbinding(_:).md)
  Returns an array describing the options for the specified binding.
- [func infoForBinding(NSBindingName) -> [NSBindingInfoKey : Any]?](nsobject-swift.class/infoforbinding(_:).md)
  Returns a dictionary describing the receiver’s `binding`.
- [struct NSBindingInfoKey](../AppKit/NSBindingInfoKey.md)
- [func NSIsControllerMarker(_ object: Any?) -> Bool](../AppKit/NSIsControllerMarker(_:).md)
  Tests whether a given object is special marker object used for indicating the state of a selection in relation to a key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/unbind(_:))*